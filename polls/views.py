from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Criar uma visualização para a página inicial
def index(request): # 'request' quando estiver fazendo uma tentativa de acessar o site
    return HttpResponse("Olá, esse é o meu primeiro site")
