from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^credito/$', views.get_creditos_view, name='credito'),
    url(r'^credito/(?P<id_empresa>\w+)/$', views.get_creditos_clientes_empresa_view, name='creditos_empresa'),
]