from django.http import HttpResponse
import socket


def home(request):
    # Obter o nome do host ou IP do cliente
    # hostname = socket.gethostname()     
    # message = f"Olá, visitante de {hostname}! - Create by Elias"
    message = ("<body bgcolor='brown'><h1>Olá, seja bem vindo(a) ao meu projeto Django - Create by Vinicius</h1></body>")
    return HttpResponse(message)