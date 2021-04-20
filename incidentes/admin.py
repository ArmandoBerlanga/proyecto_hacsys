from incidentes.models import Accion, Incidente, Persona
from django.contrib import admin

# Register your models here.
admin.site.register(Persona)
admin.site.register(Incidente)
admin.site.register(Accion)