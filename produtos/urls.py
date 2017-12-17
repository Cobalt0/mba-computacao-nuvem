# connectedin/perfis/urls.py 
from django.conf.urls import url
from produtos import views
from views import RegistrarProdutoView

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^cadastrar/$', RegistrarProdutoView.as_view(), name="cadastrar"),
    url(r'^consultar$',  views.listar, name='listar'),
]