from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def contato(request):
    pagina = ('<body bgcolor="#FFF8DC"><h1>Python</h1><p>vinicius@gmail.com</h1>')
    return HttpResponse(pagina)

