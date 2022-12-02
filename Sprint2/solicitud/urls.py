from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^solicitud/$', views.documentView, name='solicitud'),
    url(r'^solicitud/(?P<id_empresa>\w+)/$', views.solicitudes_empresa, name='solicitudes_empresa'),
]