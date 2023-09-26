from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('hola mundo desde django')

def despedida(request):
    return HttpResponse('adios desde django')

def contacto(request):
    return HttpResponse('contacto@gmail.com, tel: 5555')