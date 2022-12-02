from django import forms

class SolicitudForm(forms.Form):
    documentoCliente = forms.FileField(label='Select a file')
    cedula = forms.FloatField(label='Digite su cedula')