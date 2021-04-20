from django.db.models import fields
from django.db.models.enums import IntegerChoices
from django.forms import EmailInput
from incidentes.models import Incidente, Persona
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

            "fecha" : EmailInput(attrs = {"type" : "date"})
        }