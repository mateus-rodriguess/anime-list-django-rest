import requests
import json
import traceback
import os, sys


def token_user():
    """
    função que faz a autenticação por meio de token
    """
    # recomeda que esses dados esteja em um arquivo separado
    data = {
        "username": "user",
        "password": "senha"
    }
  
    try:
        # url pra autenticação
        url = "https://anime-list-django.herokuapp.com/api-token-auth/"
        response = requests.post(url, data=data)
        # pegando o token da resposta
        token = json.loads(response.text).get('token')
        print(f"token: {token}")
    except:
        print(traceback.format_exc())
        print("verifica o arquivo ou nome e saia daqui")
        # sair
        sys.exit()

    return token


def data():
    """
    função que manda os dados pra a API
    """
    token = None
    # dados do anime
    # a api não permite nomes de animes iguais 
    data = {
        "title" : "Horimiya",
        "episodes" : "12",
        "description" : "On the surface, the thought of Kyouko Hori and Izumi Miyamura getting...",
        "genres" : "Slice of Life, Comedy, Romance, School, Shounen",
        "studios" : "CloverWorks",
        "popularity" : "360",
        "mean_score" : "371.253",
        "average_score" : "9.407",
        "your_note" : "12",
    }   

    token = token_user()

    if token:
        token = f"Token {token}"
        headers = {"Authorization": token}
        # add o anime
        response = requests.post("https://anime-list-django.herokuapp.com/api/animes/",data=data, headers=headers)
        print(f">: {response}")
        # suporta os metodos delete, editar
        # editar
        #   response = requests.post("https://anime-list-django.herokuapp.com/api/animes/<id do anime>/",data=data, headers=headers)
        # apagar
        #   response = requests.delete("https://anime-list-django.herokuapp.com/api/animes/<id do anime>/",headers=headers)
        # listar
        response = requests.get("https://anime-list-django.herokuapp.com/api/animes/?format=json", headers=headers)
        print(response.text)
    else:
        print('token regeitado')


if __name__ == "__main__":
    data()