from django.conf.urls import patterns, url
from django.contrib import admin
from produtos import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^$', views.listar, name='listar')
]
