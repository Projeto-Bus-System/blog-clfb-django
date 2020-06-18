from django.shortcuts import render

from paginas.forms import CriarPaginaForms
from paginas.models import Paginas

# Create your views here.
def index(request):
    context = {}
    
    minhas_paginas = Paginas.objects.all()
    context['paginas'] = minhas_paginas

    return render(request, 'index.html', context=context)

def criar(request):
    context = {}

    if request.method == 'POST':
        form = CriarPaginaForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CriarPaginaForms()
    
    context['form'] = form
    
    return render(request, 'criar.html', context=context)
    
def detalhes(request, id):
    context = {}
    context['pagina'] = Paginas.objects.get(pk=id)

    return render(request, 'detalhes.html', context=context)

def remove(request, id):
    context = {}
    context['pagina'] = Paginas.objects.get(pk=id) # consulte documentacao do django e veja como apagar... precisa fazer a rota - urls.py
    
    return render(request, 'remove.html', context=context)

def editar(request, id):
    context = {}
    pagina = Paginas.objects.get(pk=id)
    context['pagina'] = pagina
    # implementar editar... parecido com criar...  
    form = CriarPaginaForms(instance=pagina)
    # escrever a logica de negocios para salvar o item editado...
    context['form'] = form

    return render(request, 'editar.html', context=context)
