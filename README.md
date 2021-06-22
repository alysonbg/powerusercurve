# powerusercurve
[![Python application](https://github.com/alysonbg/powerusercurve/actions/workflows/django_project.yml/badge.svg)](https://github.com/alysonbg/powerusercurve/actions/workflows/django_project.yml)

Desafio técnico do cíngulo
## Como rodar a aplicação(python 3.9):
1. Clone o repositório.
2. Instale o pipenv
3. Ative o virtualenv.
4. Instale as depedências.
5. Inicie o container do postgresql   
6. Configure a instância com o .env
7. Execute as migrações
8. Execute os testes
9. Importar os dados
10. Executar a aplicação

```console
git clone git@github.com:alysonbg/powerusercurve.git
cd powerusercurve
pip install pipenv
pipenv sync -d
docker-compose up -d
cp contrib/env-sample .env
pipenv run python manage.py migrate
pipenv run pytest
pipenv run python manage.py importdata
pipenv run python manage.py runserver
```

## Como acessar os endpoints:
1. Crie um usuário novo.
2. Faça uma requisição para conseguir um novo token
3. Salve o token.

```console
pipenv python manage.py createsuperuser admin
curl -d 'username=usuario&password=senha' http://127.0.0.1:8000/api-token-auth/
```

## Endpoints:
/api-token-auth/
```console
curl -d 'username=usuario&password=senha' http://127.0.0.1:8000/api-token-auth/
```

Endpoint para criar ou retornar um token.

/api/users/<int:user_id>/
```console
curl -H "Authorization: Token seu token"  http://127.0.0.1:8000/api/users/1
```

Endpoint que lista as atividades de um usuário

/api/users/activities/?day=2021-01-01
```console
curl -H "Authorization: Token afc41bb1e8627340788a81f02a8ad828f11b5d3b" http://127.0.0.1:8000/api/users/activities/?day=2021-01-01
```

Endpoint que lista a quantidade de usuários que utilizaram o app em um dia.

/api/users/activities/month/?month=5
```console
curl -H "Authorization: Token afc41bb1e8627340788a81f02a8ad828f11b5d3b" http://127.0.0.1:8000/api/users/activities/month/?month=1
```
Endpoint que lista a quantidade de usuários que usaram o app em cada dia de um mês.

## Ambiente de trabalho:

Sistema Operacional: Linux mint 20.1

IDE: Pycharm 2021.1.2

Python: 3.9.5