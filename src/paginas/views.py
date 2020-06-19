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
    pagina = Paginas.objects.get(pk=id)
    context['pagina'] = pagina

    form_bd = CriarPaginaForms(request.POST or None,instance=pagina)
    # implementar editar... parecido com criar...  
    # escrever a logica de negocios para salvar o item editado...

    #print(form_bd)
    if form_bd.is_valid():
        
        titulo = form_bd.cleaned_data['titulo']
        dono = form_bd.cleaned_data['dono'] 
        conteudo = form_bd.cleaned_data['conteudo']
        
        
        tarefa_nova = Paginas(titulo=titulo,dono=dono, conteudo=conteudo)
        form_bd = tarefa_nova
        form_bd.save(force_update=True)
        print('Sou o form bd',form_bd)
    else:
        print('falso')

    context['form'] = form_bd

    return render(request, 'editar.html', context=context)
