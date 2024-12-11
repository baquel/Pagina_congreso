from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def resumenes(request):
    return HttpResponse("Vista resumenes")

def autores(request):
    return HttpResponse("Vista autores")

def revisores(request):
    return HttpResponse("Vista revisores")