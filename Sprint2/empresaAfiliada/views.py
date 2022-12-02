from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EmpresaAfiliadaForm
from .logic.empresaAfiliada_logic import get_empresaAfiliadas, create_empresaAfiliada

def empresaAfiliada_list(request):
    empresaAfiliadas = get_empresaAfiliadas()
    context = {
        'empresaAfiliada_list': empresaAfiliadas
    }
    return render(request, 'EmpresaAfiliada/empresaAfiliada.html', context)

def empresaAfiliada_create(request):
    if request.method == 'POST':
        form = EmpresaAfiliadaForm(request.POST)
        if form.is_valid():
            create_empresaAfiliada(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created empresaAfiliada')
            return HttpResponseRedirect(reverse('empresaAfiliadaCreate'))
        else:
            print(form.errors)
    else:
        form = EmpresaAfiliadaForm()

    context = {
        'form': form,
    }
    return render(request, 'EmpresaAfiliada/empresaAfiliadaCreate.html', context)
