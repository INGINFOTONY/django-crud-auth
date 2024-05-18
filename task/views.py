from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import MateriasForm
from .forms import AlumnosForm
from .models import Materias
from .models import Alumnos
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro de usuario #
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
    return render(request, 'signup.html', {
        'form': UserCreationForm,
        "error": 'Las contraseñas no coinciden'
    })

#Lista materias
def tasks(request):
    busqueda = request.GET.get('buscar')
    lista = Materias.objects.all()
    if busqueda:
        lista = Materias.objects.filter(
            Q(nom_materia__icontains = busqueda) |
            Q(clave_mat__icontains = busqueda)
        ).distinct()
    return render(request, 'tasks.html',{
        'lista':lista
    })

# Lista alumnos


def crear_alumno(request):
    return render(request,'crear_alumno.html')

def tasksa(request):
    busqueda = request.GET.get('buscar')
    lista_A = Alumnos.objects.all()
    if busqueda:
        lista_A = Alumnos.objects.filter(
            Q(nom_alumno__icontains = busqueda) |
            Q(num_control__icontains = busqueda)
        ).distinct()
    return render(request,'tasksa.html',{
        'lista_A': lista_A
    })

def crear_alumno(request):
    if request.method == 'GET':
        return render(request,'crear_alumno.html',{
            'form': AlumnosForm
        })
    else:
        try:
            form = AlumnosForm(request.POST)
            nuevo_alum = form.save(commit=False)
            nuevo_alum.save()
            return redirect('tasksa')
        except ValueError:
            return render (request,'tasksa.html',{
                'form': AlumnosForm,
                'error': 'Ingresar datos validos'
            })

def eliminar_alumnos(request, alumno_id):
    try: 
        alumno = Alumnos.objects.get(pk=alumno_id)
        alumno.delete()
    except Alumnos.DoesNotExist:
        pass
    return redirect('tasks')

def editar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumnos, pk=alumno_id)
    if request.method == 'POST':
        form1 = AlumnosForm(request.POST, instance=alumno)
        if form1.is_valid():
            form1.save()
            return redirect('tasksa')
    else:
        form1 = AlumnosForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form1': form1})




#Vista Crear materia
def crear_materia(request):
    if request.method == 'GET':
        return render(request,'crear_materia.html',{
        'form' : MateriasForm
    })
    else:
        try:
            form = MateriasForm(request.POST)
            nueva_mat = form.save(commit=False)
            nueva_mat.user = request.user
            nueva_mat.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'crear_materia.html', {
                'form': MateriasForm,
                'error': 'Ingresa datos validos'
            })
        
def eliminar_materia(request, materia_id):
    try:
        materia = Materias.objects.get(pk=materia_id)
        materia.delete()
    except Materias.DoesNotExist:
        pass

    return redirect('tasks')

def editar_materia(request, materia_id):
    materia = get_object_or_404(Materias, pk=materia_id)

    if request.method == 'POST':
        form = MateriasForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = MateriasForm(instance=materia)

    return render(request, 'editar_tarea.html', {'form': form})


#login

def singout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')
     



#buscador $


