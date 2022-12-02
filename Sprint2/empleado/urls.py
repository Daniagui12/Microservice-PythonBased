from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('empleado/', views.empleado_list),
    path('empleadocreate/', csrf_exempt(views.empleado_create), name='empleadoCreate'),
]