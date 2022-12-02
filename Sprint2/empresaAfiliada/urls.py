from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('empresaAfiliada/', views.empresaAfiliada_list, name='empresaAfiliadaList'),
    path('empresaAfiliadacreate/', csrf_exempt(views.empresaAfiliada_create), name='empresaAfiliadaCreate'),
]