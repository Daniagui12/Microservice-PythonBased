import datetime
import json
from django.shortcuts import redirect, render
from .models import Solicitud
from .forms import SolicitudForm
from empleado.logic.logic_empleado import get_empleado_by_cedula
from solicitud.logic.logic_solicitud import detect_text
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from .logic.logic_solicitud import get_solicitudes_clientes_empresa, get_solicitudes
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Sprint2.auth0backend import getRole
from django.views.decorators.csrf import csrf_exempt
import traceback

@csrf_exempt
def documentView(request):
    try:
        role = getRole(request)
        # Handle file upload
        if request.method == 'GET':
            if role in ['CEO Avanzo']:
                # Get data in json
                solicitudes = get_solicitudes()
                return JsonResponse({"Solicitudes": list(solicitudes)})
            else:
                return HttpResponse('Unauthorized Role', status=401)

        elif request.method == 'POST':
            if role in ['Empleado']:
                message = 'Suba el documento a analizar'
                # form = SolicitudForm(request.POST, request.FILES)
                # if form.is_valid():
                dateToday = datetime.datetime.now()
                cliente = get_empleado_by_cedula(request.POST['cedula'])
                newdoc = Solicitud(documentoCliente=request.FILES['documentoCliente'], id_cliente=cliente, fechaCreacion=dateToday, estado="Pendiente")
                newdoc.save()
                confidence = detect_text(newdoc.documentoCliente.path)
                if confidence < 0.96:
                    newdoc.estado = "Rechazado"
                    newdoc.save()
                    message = 'El documento no es legible - Confidence: {}%'.format(round(confidence*100,2))
                    return HttpResponse(message)
                else:
                    newdoc.estado = "Aprobado"
                    newdoc.save()
                    message = 'El documento es legible - Confidence: {}%'.format(round(confidence*100,2))
                    return HttpResponse(message)

                # Redirect to the document list after POST
                # else:
                #     message = 'The form is not valid. Fix the following error:'
            else:
                return HttpResponse('Unauthorized Role', status=401)

    except Exception as e:
        print(e)
        return HttpResponse('Unauthorized Token', status=401)

def solicitudes_empresa(request, id_empresa):
    try:
        role = getRole(request)
        if role in ['CEO Avanzo', 'Gerente Empresa Aliada']:
            solicitudes = get_solicitudes_clientes_empresa(id_empresa)
            return JsonResponse({"Solicitudes por empresa": list(solicitudes)})
        else:
            return HttpResponse('Unauthorized Role', status=401)
    except Exception as e:
        print(e)
        return HttpResponse('Unauthorized Token', status=401)




