import json
from django.shortcuts import render
from .forms import EmpleadoForm
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_empleado import create_empleado, get_empleados, filter_empleados_by_empresaAfiliada
from .filters import EmpleadoFilter
from Sprint2.auth0backend import getRole

def empleado_list(request):
    try:
        role = getRole(request)
        if role in ['CEO Avanzo']:       
            empleados = get_empleados()
            qs_json = json.dumps(list(empleados), cls=DjangoJSONEncoder)
            return HttpResponse(qs_json, content_type='application/json')

        else:
            return HttpResponse('Unauthorized Role', status=401)
            
    except Exception as e:
        print(e)
        return HttpResponse('Unauthorized Token', status=401)

def empleado_filter(request, empresaAfiliada):
    empleados = filter_empleados_by_empresaAfiliada(empresaAfiliada)
    context = {
        'empleado_list': empleados
    }
    return render(request, 'Empleado/empleado.html', context)

def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            create_empleado(form)
            messages.add_message(request, messages.SUCCESS, 'empleado create successful')
            return HttpResponseRedirect(reverse('empleadoCreate'))
        else:
            print(form.errors)
    else:
        form = EmpleadoForm()

    context = {
        'form': form,
    }

    return render(request, 'Empleado/empleadoCreate.html', context)
    