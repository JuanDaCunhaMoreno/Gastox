# 💸 Gastox

Sistema simples de controle de gastos pessoais via terminal, com suporte a cadastro, edição, exclusão, estatísticas e exportação de dados.

---

## 🧾 Funcionalidades

- ✅ Cadastrar novos gastos
- ✏️ Editar gastos existentes
- ❌ Remover gastos por ID
- 📋 Listar todos os gastos
- 📊 Exibir total por categoria
- 📈 Estatísticas gerais (total, média, maior e menor gasto)
- 📤 Exportar dados para CSV # AINDA não está 100% funcional
- 🔐 IDs únicos 

---

## 🖥️ Interface (menu via terminal)

- 1 - Cadastrar gasto
- 2 - Editar gasto
- 3 - Remover gasto
- 4 - Listar gastos
- 5 - Exibir total por categoria
- 6 - Estatísticas gerais
- 7 - Exportar dados
- 0 - Sair

---

## 🧱 Estrutura do Projeto

Gastox/
├── main.py # Ponto de entrada e menu
├── models.py # Classe Despesa
├── database.py # Funções CRUD
├── relatorios.py # Estatísticas e totais
├── exportador.py # Exportação para CSV
├── README.md # Este arquivo