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
    
    
    

    if request.method =='POST':
        pagina_del = Paginas.objects.all()
        pagina_del.filter(id=id).delete()

    return render(request, 'remove.html', context=context)

def editar(request, id):
    context = {}
    pagina = Paginas.objects.get(id=id)
    form_bd = CriarPaginaForms(instance=pagina)
    form_nova = CriarPaginaForms(instance=pagina)
    context['pagina'] = pagina
    # implementar editar... parecido com criar...  
    # escrever a logica de negocios para salvar o item editado...

    
    if form_nova.is_valid():
        form_bd = form_nova
        form_bd.save(force_update=True)

    context['form'] = form_nova

    return render(request, 'editar.html', context=context)
