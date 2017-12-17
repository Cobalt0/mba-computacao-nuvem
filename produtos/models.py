from django.db import models

class Produto(models.Model):
	nome_produto = models.CharField(max_length=255, null=False)
	descricao = models.CharField(max_length=255, null=False)
	grupos = models.CharField(max_length=255, null=False)
	codigo_barras = models.PositiveIntegerField(default=0)
	unidade = models.CharField(max_length=2, null=False)
	peso = models.FloatField(default=0)
	estoque = models.PositiveIntegerField(default=0)
	valor = models.FloatField()