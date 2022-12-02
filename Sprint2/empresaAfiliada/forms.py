from django import forms
from .models import EmpresaAfiliada

class EmpresaAfiliadaForm(forms.ModelForm):
    class Meta:
        model = EmpresaAfiliada
        fields = [
            'nombre',
            'NIT',
            'temporalidadContrato',
            'formatoDocumento',
        ]
        labels = {
            'nombre' : 'Nombre',
            'NIT' : 'NIT',
            'temporalidadContrato' : 'Temporalidad Contrato',
            'formatoDocumento' : 'Formato Documento',
        }