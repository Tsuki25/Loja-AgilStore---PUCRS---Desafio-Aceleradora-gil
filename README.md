# Loja-AgilStore---PUCRS---Desafio-Aceleradora-gil

## Descrição

O desafio proposto foi concluído seguindo todas as orientações desejadas, optei por realizar a implementação utilizando o Framework Flask para aproveitar conhecimentos previos, bem como a estrutura html que já possuia de outros projetos desenvolvidos, desta forma fui capaz de apresentar todas as funcionalidades solicitadas com uma adição de qualidade da visualização com um front-end bem trabalhado.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python.
- **Python 3.11.1**: Linguagem de programação utilizada.
- **Jinja2**: Template engine que o Flask usa para renderizar HTML.
- **SQLite**: Banco de dados leve (caso esteja usando um banco local).
- **Werkzeug**: Conjunto de ferramentas para aplicações web.

## Requisitos

Antes de rodar a aplicação, você precisará instalar as dependências listadas no arquivo `requirements.txt`.

## Como Rodar a Aplicação Localmente

1. **Clone o repositório** para sua máquina:

   ```bash
   git clone https://github.com/seu-usuario/fLoja-AgilStore---PUCRS---Desafio-Aceleradora-gil.git

   cd flask-project

   * Crie a venv
      python -m venv venv
      .\venv\Scripts\activate

   * Instale as dependencias
      pip install -r requirements.txt

   * Inicie a aplicação web e acesse o endereço local
      flask run

## Estrutura do Projeto

- **app.py**: Arquivo principal que contém as rotas e lógica da aplicação.
- **requirements.txt**: Arquivo contendo as dependências do projeto.
- **templates/**: Diretório onde os arquivos HTML são armazenados.
- **static/**: Diretório onde arquivos estáticos como CSS, JS, e imagens são armazenados.

## Rotas

- **GET /**: Página inicial.
- **GET /listar_produtos**: Lista todos os produtos.
- **GET /buscar_produtos**: Busca produtos.
- **POST /adicionar_produto**: Adiciona um novo produto
