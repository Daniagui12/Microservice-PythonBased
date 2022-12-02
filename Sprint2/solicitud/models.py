from django.db import models
from empleado.models import Empleado

# Create your models here.
class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Empleado, on_delete=models.CASCADE, default=None)
    fechaCreacion = models.DateField()
    estado = models.CharField(max_length=20)
    documentoCliente = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_solicitud)