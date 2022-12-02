from django import forms
from .models import Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'empresaAfiliada',
            'nombre',
            'sueldo',
            'inicioContrato',
            'descuentoRealizado',
            'numeroDocumento',
            'tipoDocumento',
            #'dateTime',
        ]

        labels = {
            'empresaAfiliada' : 'Empresa Afiliada',
            'nombre' : 'Nombre',
            'sueldo' : 'Sueldo',
            'inicioContrato' : 'Inicio del contrato',
            'descuentoRealizado' : 'Descuento Realizado',
            'numeroDocumento' : 'Numero Documento',
            'tipoDocumento' : 'Tipo Documento',
            #'dateTime' : 'Date Time',
        }