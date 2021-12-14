from django.shortcuts import render
from django.template import  Template, Context
from django.http import HttpResponse

# Create your views here.

def vista_login(request):
    documento = open("C:/Users/ADMIN/PycharmProjects/Cafeteria/")
    t = Template(documento.read())
    documento.close()
    c = Context()
    return  HttpResponse(t.render(c))

def vista_Registro(request):
    document = open("C:/Users/ADMIN/PycharmProjects/Cafeteria/templates/Registro.html")
    t = Template(document.read())
    document.close()
    c = Context()
    return  HttpResponse(t.render(c))
