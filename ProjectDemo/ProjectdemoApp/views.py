from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "ProjectdemoApp/home.html")


def servicios(request):
    return render(request, "ProjectdemoApp/servicios.html")


def tienda(request):
    return render(request, "ProjectdemoApp/tienda.html")


def blog(request):
    return render(request, "ProjectdemoApp/blog.html")


def contacto(request):
    return render(request, "ProjectdemoApp/contacto.html")
