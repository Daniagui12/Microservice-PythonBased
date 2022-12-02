import django_filters
from django_filters import CharFilter, NumberFilter

from .models import *

class EmpleadoFilter(django_filters.FilterSet):
    
    nombre = CharFilter(field_name='nombre', lookup_expr='icontains')
    documento = NumberFilter(field_name='numeroDocumento', lookup_expr='icontains')

    class Meta:
        model = Empleado
        fields = ['empresaAfiliada', 'nombre']
