from django.urls import path
from .import views 

urlpatterns = [
    path('',views.home),
    path('registrarCurso/',views.RegistrarCurso),
    path('eliminarCurso/<codigo>',views.EliminarCurso)


]
