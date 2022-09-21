# luizacode-projeto2
## Carrinho de Compras (Projeto 2) - Luiza Code
Projeto do bootcamp Luiza Code do Magazine Luiza.

Desenvolvimento de uma API de carrinho de compras, com persistência de dados no MongoDB.

## Opções da API:
A API permite a criação e exclusão dos registros abaixo, além de várias opções de consulta.
* Produtos
* Usuários
* Endereços
* Carrinho

## Dependências
* PyMongo - Bilbioteca Python utilizada para trabalho com o MongoDB no Python.
* Motor - Driver oficial do MongoDB para trabalhar de forma assíncrona.
* FastAPI - Framework Python utilizado no desenvolvimento de API's.
* Pydantic - Biblioteca que implementa a validação de dados para Python.
* Uvicorn - Framework que dá a base dos componentes assíncronos do FastAPI.

## Documentação
A documentação da API está em construção.</br>
* Após iniciar o servidor da API, a documentação ficará disponível no endereço:</br>
http://localhost:8000/docs
</br>

## Instalação (Windows)
* Criar ambiente virtual
    ```
    $ python -m venv venv
    ```
* Ativar ambiente

    ```
    $ .\venv\Scripts\Activate.ps1
    ```
* Instalar dependências
     ```
     $ pip install -r requirements.txt
     ```
* Iniciar o servidor
    ```
    uvicorn main:app --reload
    ```