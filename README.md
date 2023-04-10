## Sistema desenvolvido com Django Rest Framework que permite o controle de usuários e pedidos.

## Instruções para rodar a aplicação

### Pré Requisitos

- É necessário ter instalado o Docker na sua máquina

### Passo a passo para rodar a aplicação

1 - Clone o repositório

#### Na raiz do projeto, execute o seguinte comando para construir as imagens Docker:

2 - docker-compose up -d --build 

#### Execute as migrações do Django para criar as tabelas do banco de dados:

3 - docker-compose exec web python manage.py migrate 

#### Crie um superusuário para acessar a aplicação:

4 - docker-compose exec web python manage.py createsuperuser

Depois acesse o sistema pelo navegador: http://127.0.0.1:8000/

Será necessário fazer o login em http://127.0.0.1:8000/admin

#### Documentação da api com endpoints podem ser acessadas

- /Swagger/ - Documentação da API usando o Swagger UI;
- /Redoc/  - Documentação da API usando o ReDoc.

#### Para rodar os testes, execute o comando: 

docker-compose exec web python manage.py test
