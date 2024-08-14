from django import froms
from .models import Producto

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fiels = ['nombre', 'descripcion','precio', 'stock']
        

