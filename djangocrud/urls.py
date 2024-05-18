"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasksa/', views.tasksa, name='tasksa'),
    path('tasks/crear/', views.crear_materia, name='crear_materia'),
    path('tasksa/crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('tasksa/eliminar_alumno/<int:alumno_id>/', views.eliminar_alumnos, name='eliminar_alumno'),
    path('tasks/eliminar/<int:materia_id>/', views.eliminar_materia, name='eliminar_materia'),
    path('tasks/editar/<int:materia_id>/', views.editar_materia, name='editar_materia'),
    path('tasksa/editar/<int:alumno_id>/', views.editar_alumno, name='editar_alumno'),
    path('logout/', views.singout, name='logout'),
    path('signin/', views.signin, name='signin'),

]
