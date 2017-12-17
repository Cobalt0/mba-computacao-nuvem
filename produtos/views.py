from django.shortcuts import render, redirect
from django.http import HttpResponse
from produtos.models import Produto
from produtos.forms import RegistrarPordutos
from django.views.generic.base import View

def index(request):
    return render(request, 'index.html')

def get(self, request, *args, **kwargs):
		return render(request, self.template_name)


def listar(request):
    return render(request, 'listar.html', {'produtos' : Produto.objects.all()})


class RegistrarProdutoView(View):
	
	template_name = 'cadastro_produto.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
		
	def post(self, request, *args, **kwargs):

		form = RegistrarPordutos(request.POST)

		dados_form = form.data

		produto = Produto(nome_produto=dados_form['nomeProduto'], 
							descricao=dados_form['descricao'], 
							grupos=dados_form['grupo'], 
							codigo_barras=dados_form['codigoBarras'], 
							unidade=dados_form['unidade'], 
							peso=dados_form['peso'], 
							estoque=dados_form['estoque'], 
							valor=dados_form['valor'])
		produto.save()

		return redirect('index')
