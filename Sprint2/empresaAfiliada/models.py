from django.db import models

class EmpresaAfiliada(models.Model):
    nombre = models.CharField(max_length=50)
    NIT = models.CharField(max_length=50, primary_key=True)
    temporalidadContrato = models.IntegerField(null=True, blank=True, default=None)
    formatoDocumento = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
