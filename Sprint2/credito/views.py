import json
from django.http import HttpResponse
from credito.logic.logic_credito import get_creditos_clientes_empresa, get_creditos
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Sprint2.auth0backend import getRole

def get_creditos_view(request):
    try:
        role = getRole(request)
        if role in ['CEO Avanzo', 'Gerente Empresa Aliada']:
            creditos = get_creditos()
            return JsonResponse({"Creditos totales": list(creditos)})
        else:
            return HttpResponse('Unauthorized Role', status=401)
    
    except Exception as e:
        print(e)
        return HttpResponse('Unauthorized Token', status=401)

def get_creditos_clientes_empresa_view(request,id_empresa):
    try:
        role = getRole(request)
        if role in ['CEO Avanzo', 'Gerente Empresa Aliada']:
            creditos = get_creditos_clientes_empresa(id_empresa)
            return JsonResponse({"Creditos por empresa": list(creditos)})
        else:
            return HttpResponse('Unauthorized Role', status=401)

    except Exception as e:
        print(e)
        return HttpResponse('Unauthorized Token', status=401)


