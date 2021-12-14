from django.template import  Template, Context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
# Create your views here.


@login_required()
def vista_Menu(request):
    documento = open("C:/Users/ADMIN/PycharmProjects/Cafeteria/templates/Menu.html")
    t = Template(documento.read())
    documento.close()
    c = Context()
    return  HttpResponse(t.render(c))



def buscar_prod(request):
    return render(request, "buscar.html")