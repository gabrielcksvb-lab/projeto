Mini Sistema de Cadastro e Controle

Gabriel Silva

Este é um sistema de gerenciamento de cadastros desenvolvido em Python utilizando o framework web Django. O objetivo principal é permitir o controle eficiente de Clientes e seus respectivos Pedidos através de uma interface administrativa intuitiva. O sistema implementa conceitos essenciais como Programação Orientada a Objetos (POO), persistência de dados em banco relacional (SQLite) e rotinas completas de CRUD.

Funcionalidades:
- Cadastro de novos clientes (com validação de e-mail único).
- Listagem e visualização de clientes cadastrados.
- Criação de pedidos vinculados a um cliente específico (Relação 1:N).
- Edição e exclusão de registros (CRUD Completo).
- Validação de regras de negócio (ex: bloqueio de pedidos com valor negativo).

Tecnologias Utilizadas:
- Linguagem: Python 3
- Framework Web: Django
- Banco de Dados: SQLite3
- Controle de Versão: Git e GitHub

Como Executar o Projeto:
Siga o passo a passo abaixo para rodar o projeto localmente:

1. Clone este repositório para o seu computador: 
   git clone [https://github.com/gabrielcksvb-lab/projeto.git](https://github.com/gabrielcksvb-lab/projeto.git)

2. Pelo terminal, acesse a pasta do projeto:
    cd projeto

3. Crie e ative um ambiente virtual:
    python -m venv venv
    venv\Scripts\activate

4. Instale o Django:
    pip install django

5. Execute as migrações para preparar o banco de dados:
    python manage.py migrate

6. Inicie o servidor local:
    python manage.py runserver

7. Acesse o sistema no navegador através do endereço http://127.0.0.1:8000/admin.

Obs.:  Ajuste no `.gitignore`
Se a linha `*.sqlite3` ou `db.sqlite3` estiver lá, **apague-a**. Deixe o arquivo apenas com itens de cache e ambiente, assim:

__pycache__/
venv/