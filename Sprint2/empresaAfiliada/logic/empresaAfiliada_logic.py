from ..models import EmpresaAfiliada

def get_empresaAfiliadas():
    queryset = EmpresaAfiliada.objects.all()
    return (queryset)

def create_empresaAfiliada(form):
    empresaAfiliada = form.save()
    empresaAfiliada.save()
    return ()