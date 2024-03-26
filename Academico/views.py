from django.shortcuts import render,redirect
from .models import Curso

# Create your views here.
def home(request):
    cursolista=Curso.objects.all()
    return render (request,'gestionCursos.html',{'cursos':cursolista})

def RegistrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['txtCreditos']
    curso=Curso.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')

def EliminarCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')
    
