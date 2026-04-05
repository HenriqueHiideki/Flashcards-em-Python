# 📚 Sistema de Flashcards com Repetição Espaçada

Este projeto é um programa em Python que implementa um sistema simples de **flashcards com repetição espaçada**, ajudando no aprendizado e memorização de conteúdos ao longo do tempo.

---

## 🚀 Funcionalidades

- ➕ Adicionar novos flashcards (pergunta e resposta)
- 🔁 Revisar flashcards com base na data atual
- 📈 Ajustar automaticamente o intervalo de revisão conforme o desempenho
- 💾 Armazenamento dos dados em arquivo JSON

---

## 🧠 Como funciona

O sistema utiliza um modelo básico de **repetição espaçada**:

- Cada flashcard possui um intervalo de revisão (em dias)
- Ao revisar:
  - ✅ Se o usuário **acertar**, o intervalo dobra (ex: 1 → 2 → 4 → 8 dias)
  - ❌ Se o usuário **errar**, o intervalo volta para 1 dia
- O programa mostra apenas os flashcards que precisam ser revisados no dia

---

## 📁 Estrutura do Projeto
