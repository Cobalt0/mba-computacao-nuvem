from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def listar(request):
	return render(request, 'listar.html')