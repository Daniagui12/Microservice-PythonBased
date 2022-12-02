from credito.models import Credito
from empleado.models import Empleado
from empresaAfiliada.models import EmpresaAfiliada

def get_creditos():
    queryset = Credito.objects.values()
    return queryset

def filter_creditos_by_id_cliente(id_cliente):
    queryset = Credito.objects.filter(id_cliente=id_cliente)
    return (queryset)

def create_credito(form):
    credito = form.save()
    credito.save()
    return ()

def get_creditos_clientes_empresa(id_empresa):
    querysetEmpresa = EmpresaAfiliada.objects.get(NIT=id_empresa)
    querysetEmpleado = Empleado.objects.filter(empresaAfiliada=querysetEmpresa).values_list('id', flat=True)
    queryset = Credito.objects.filter(id_cliente_id__in = querysetEmpleado).values()
    return (queryset)

def update_credito(form, id_Credito):
    Credito = Credito.objects.get(id_Credito=id_Credito)
    Credito.id_cliente = form.cleaned_data['id_cliente']
    Credito.fechaCreacion = form.cleaned_data['fechaCreacion']
    Credito.estado = form.cleaned_data['estado']
    Credito.documentoCliente = form.cleaned_data['documentoCliente']
    Credito.save()
    return ()

def delete_credito(id_Credito):
    Credito = Credito.objects.get(id_Credito=id_Credito)
    Credito.delete()
    return ()