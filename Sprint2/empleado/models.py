from django.db import models
from empresaAfiliada.models import EmpresaAfiliada

DOCUMENTO_CHOICES = (
    ('cedula','CEDULA'),
    ('pasaporte','PASAPORTE'),
)


class Empleado(models.Model):
    empresaAfiliada = models.ForeignKey(EmpresaAfiliada, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=50)
    sueldo = models.FloatField(null=True, blank=True, default=None)
    inicioContrato = models.DateField(null=True, blank=True, default=None)
    descuentoRealizado = models.FloatField(null=True, blank=True, default=None)
    numeroDocumento = models.FloatField(null=True, blank=True, default=None)
    tipoDocumento = models.CharField(max_length=50, choices=DOCUMENTO_CHOICES, default='cedula')

    def __str__(self):
        return '%s %s' % (self.nombre, self.numeroDocumento)
