from django.shortcuts import render, HttpResponse
from servicios.models import Servicio


# Create your views here.
def home(request):
    return render(request,'django_project_app/home.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request,'django_project_app/servicios.html', {"servicios": servicios})

def tienda(request):
    return render(request,'django_project_app/tienda.html')

def blog(request):
    return render(request,'django_project_app/blog.html')

def contacto(request):
    return render(request,'django_project_app/contacto.html')