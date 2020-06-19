from django.urls import path
from paginas.views import *

urlpatterns = [
    path('', index),
    path('criar/', criar),
    path('detalhe/<int:id>/', detalhes),
    path('editar/<int:id>/', editar),
    path('deletar/<int:id>/', remove),

]


