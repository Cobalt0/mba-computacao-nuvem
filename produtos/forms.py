from django import forms

class RegistrarPordutos(forms.Form):
	nomeProduto = forms.CharField(required=True)
	descricao = forms.CharField(required=True)
	grupo = forms.CharField(required=True)
	codigoBarras = forms.IntegerField(required=True)
	unidade = forms.CharField(required=True)
	peso = forms.FloatField(required=True)
	estoque = forms.FloatField(required=True)
	valor = forms.FloatField(required=True)

	