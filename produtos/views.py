from django.shortcuts import render, redirect
from django.http import HttpResponse
from produtos.models import Produto
from produtos.forms import RegistrarPordutos
from django.views.generic.base import View

def index(request):
    return render(request, 'index.html')



def listar(request):
    return render(request, 'listar.html', {'produtos' : Produto.objects.all()})

def editar(request, produto_id):
	produto = Produto.objects.get(id=produto_id)
	return render(request, 'editar_produto.html', {'produto' : produto})

def alterar(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    
    form = RegistrarPordutos(request.POST)

    dados_form = form.data

    produto.nome_produto = dados_form['nomeProduto']
    produto.descricao = dados_form['descricao']
    produto.grupos = dados_form['grupo']
    produto.codigo_barras = dados_form['codigoBarras']
    produto.unidade = dados_form['unidade']
    produto.peso = dados_form['peso']
    produto.estoque = dados_form['estoque']
    produto.valor = dados_form['valor']
    produto.save()
    return redirect('listar')

def excluir(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete();
    return redirect('listar')

class RegistrarProdutoView(View):
	
	template_name = 'cadastro_produto.html'

	def get(self, request):
		return render(request, self.template_name)
		
	def post(self, request):

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

		#return redirect('index')
		return render(request, 'listar.html', {'produtos' : Produto.objects.all()})
