from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Materias(models.Model):
    id = models.AutoField(primary_key=True)
    nom_materia = models.CharField(max_length=100)
    clave_mat = models.CharField(max_length=20)
    creditos = models.CharField(max_length=10)
    grupo = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_materia + ' - Maestro: ' + self.user.username



class Alumnos(models.Model):
    id = models.AutoField(primary_key=True)
    nom_alumno = models.CharField(max_length=100)
    num_control = models.CharField(max_length=10, null=True)
    semestre = models.CharField(max_length=10)

def __str__(self):
    return self.nom_alumno + ' - ' + self.num_control 
