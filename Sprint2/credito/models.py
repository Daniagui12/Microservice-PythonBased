from django.db import models
from empleado.models import Empleado
from solicitud.models import Solicitud

# Create your models here.
class Credito(models.Model):
    id_credito = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Empleado, on_delete=models.CASCADE, default=None)
    id_solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE, default=None)
    valorCuota = models.IntegerField()
    plazo = models.IntegerField()
    tasa = models.IntegerField()
    fechaPago = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.id_credito)
