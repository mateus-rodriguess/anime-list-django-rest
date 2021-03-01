# API de lista de animes com Django_rest_framework
Um simples site que você pode armazenar seus animes, os animes podem ser adicionados por meio da API ou no site.
https://anime-list-django.herokuapp.com

# Register
O registro tem  que ser pelo site: https://anime-list-django.herokuapp.com/accounts/register/

# Como usar a API
No repositorio tem uma pasta chamado test, onde tem um arquivo .py que mostra um pequena amostra de como usar a API 

# Login
Para Fazer o login acesse atravez da API: https://anime-list-django.herokuapp.com/api-token-auth/ digite seu email e 
senha criados { "username": "seu_username", "password": "exemplosenha12345" }
a função te retornará, e você já estará logado { "expiry": "2021-01-29T02:56:44.924698Z", "token": "99a27b2ebe718a2f0db6224e55b622a59cc2ertcf66861c60979a25ffb4f133e" }

# Data
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
# Token    
token = f"Token {token}"
headers = {"Authorization": token}

response = requests.post("https://anime-list-django.herokuapp.com/api/animes/",data=data, headers=headers)
# Listar
response = requests.get("https://anime-list-django.herokuapp.com/api/animes/?format=json", headers=headers)
