from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
                                    
    return render(request, 'pessoas.html', {'pessoas': pessoas})