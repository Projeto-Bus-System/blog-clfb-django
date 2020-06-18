from django.urls import path
from paginas.views import index, detalhes, criar, editar

urlpatterns = [
    path('', index),
    path('criar/', criar),
    path('detalhe/<int:id>/', detalhes),
    path('editar/<int:id>/', editar)
]


