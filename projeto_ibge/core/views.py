from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()                                 
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def cadastrar_pessoa(request):
    # Primeiro passo: puxar do template para cá
    nome_pessoa = request.POST.get('nome')
    cor_pessoa = request.POST.get('cor')
    idade_pessoa = request.POST.get('idade')
    genero_pessoa = request.POST.get('genero')
    salario_pessoa = request.POST.get('salario')

    # Segundo passo: jogar daqui para o banco de dados
    Pessoa.objects.create(nome=nome_pessoa, cor=cor_pessoa, idade=idade_pessoa, genero=genero_pessoa, salario=salario_pessoa)

    # Terceiro passo: responder
    return redirect(lista_pessoas)