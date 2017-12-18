# connectedin/perfis/urls.py 
from django.conf.urls import url
from produtos import views
from views import RegistrarProdutoView

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^cadastrar/$', RegistrarProdutoView.as_view(), name="cadastrar"),
    url(r'^consultar$',  views.listar, name='listar'),
    url(r'^editar/(?P<produto_id>\d+)$', views.editar, name='editar'),
    url(r'^alterar/(?P<produto_id>\d+)$', views.alterar, name='alterar'),
    url(r'^excluir/(?P<produto_id>\d+)$', views.excluir, name='excluir'),
]