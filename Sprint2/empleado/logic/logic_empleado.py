from empleado.models import Empleado

def get_empleados():
    queryset = Empleado.objects.defer("id", "inicioContrato").values()
    return (queryset)

def filter_empleados_by_empresaAfiliada(empresaAfiliada):
    queryset = Empleado.objects.filter(empresaAfiliada=empresaAfiliada)
    return (queryset)

def get_empleado_by_cedula(cedula):
    empleado = Empleado.objects.get(numeroDocumento=cedula)
    return empleado
    
def create_empleado(form):
    empleado = form.save()
    empleado.save()
    return ()