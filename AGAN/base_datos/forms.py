from django import forms
from .models import Agenda, Herramienta, Servicio, Usuario

class ProgramarAgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['servicio', 'fecha', 'hora', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'estado': forms.Select(),
        }

class RegistroServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['cliente', 'tecnico', 'fecha', 'duracion', 'descripcion', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(),
        }

class AsignarHerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = ['nombre', 'estado', 'cantidad', 'ubicacion']

class ConfirmacionServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['estado']
        widgets = {
            'estado': forms.HiddenInput(),
        }

class RetroalimentacionForm(forms.Form):
    comentarios = forms.CharField(widget=forms.Textarea, label='Comentarios')
