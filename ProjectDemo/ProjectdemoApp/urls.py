from django.urls import path
from ProjectdemoApp import views

urlpatterns = [
    path('', views.home, name='Inicio'),
    path('servicios', views.servicios, name='Servicios'),
    path('tienda', views.tienda, name='Tienda'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto')
]
