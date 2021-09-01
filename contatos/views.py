from django.shortcuts import render
from contatos.models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, id):
    contato = Contato.objects.get(id=id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
