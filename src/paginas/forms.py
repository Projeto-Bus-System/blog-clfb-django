from django.forms import ModelForm
from paginas.models import Paginas

class CriarPaginaForms(ModelForm):
    
    class Meta:
        model = Paginas
        fields = '__all__'
