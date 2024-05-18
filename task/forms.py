from django import forms
from .models import Materias
from .models import Alumnos

class MateriasForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = ['nom_materia', 'clave_mat', 'creditos', 'grupo']
        widgets = {
            'nom_materia': forms.TextInput(attrs={'class': 'form-control'}),
            'clave_mat': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nom_alumno','num_control','semestre']
        widgets = {
            'nom_alumno': forms.TextInput(attrs={'class': 'form-control'}),
            'num_control': forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control'}),
        }