from django import forms
from django.forms import EmailInput
from django.forms.widgets import DateInput
from incidentes.models import Accion, Incidente, Persona
from django.forms.models import ModelForm


class FormsPersona (ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs = {"type" : "emial"})
        }

class FormsIncidente (ModelForm):
    class Meta:
        model = Incidente
        fields = "__all__"
        widgets = {
            "fecha" : DateInput(attrs = {"type" : "date"})
        }

class FormsAcccion (ModelForm):
    class Meta:
        model = Accion
        fields = "__all__"
        widgets = {
        }    

class InfoFiltros (forms.Form):
    fecha = forms.DateField(label ="Fecha del incidente" ,widget=forms.TextInput(attrs={'class':'datepicker'}), required=False)
    nombre_empleado = forms.CharField(label="Nombre empleado", required=False)
    descripcion_incidente = forms.CharField(label="Que la descripción contenga", required=False)
    estatus = forms.ChoiceField(choices= ((True, "Resuelto"), (False, "No resuelto"), (None, "--")), required=False)
