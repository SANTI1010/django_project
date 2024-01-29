from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'django_project_app/home.html')

def servicios(request):
    return render(request,'django_project_app/servicios.html')

def tienda(request):
    return render(request,'django_project_app/tienda.html')

def blog(request):
    return render(request,'django_project_app/blog.html')

def contacto(request):
    return render(request,'django_project_app/contacto.html')