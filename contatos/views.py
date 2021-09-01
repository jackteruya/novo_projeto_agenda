from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contatos.models import Contato
from django.core.paginator import Paginator


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 5)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, id):
    # try:
    #     contato = Contato.objects.get(id=id)
    #     return render(request, 'contatos/ver_contato.html', {
    #         'contato': contato
    #     })
    # except Contato.DoesNotExist as e:
    #     raise Http404()

    contato = get_object_or_404(Contato, id=id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
