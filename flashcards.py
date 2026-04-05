import time
import json
from datetime import datetime, timedelta

ARQUIVO = "flashcards.json"


def carregar_flashcards():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_flashcards(cards):
    with open(ARQUIVO, "w") as f:
        json.dump(cards, f, indent=4)


def adicionar_flashcard(cards):
    pergunta = input("Pergunta: ")
    resposta = input("Resposta: ")

    card = {
        "pergunta": pergunta,
        "resposta": resposta,
        "intervalo": 1,  # dias
        "proxima_revisao": str(datetime.now().date())
    }

    cards.append(card)
    salvar_flashcards(cards)
    print("Flashcard adicionado!\n")


def revisar_flashcards(cards):
    hoje = datetime.now().date()
    revisados = False

    for card in cards:
        data_revisao = datetime.strptime(card["proxima_revisao"], "%Y-%m-%d").date()

        if data_revisao <= hoje:
            revisados = True
            print(f"\nPergunta: {card['pergunta']}")
            input("Pressione ENTER para ver a resposta...")
            print(f"Resposta: {card['resposta']}")

            desempenho = input("Você acertou? (s/n): ").lower()

            if desempenho == "s":
                card["intervalo"] *= 2  # aumenta intervalo
                print("Boa! Intervalo aumentado.")
            else:
                card["intervalo"] = 1  # reseta intervalo
                print("Vamos revisar mais cedo.")

            proxima = hoje + timedelta(days=card["intervalo"])
            card["proxima_revisao"] = str(proxima)

    if not revisados:
        print("Nenhum flashcard para revisar hoje.")

    salvar_flashcards(cards)


def menu():
    cards = carregar_flashcards()

    while True:
        print("\n=== FLASHCARDS ===")
        print("1. Adicionar flashcard")
        print("2. Revisar")
        print("3. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_flashcard(cards)
        elif opcao == "2":
            revisar_flashcards(cards)
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()