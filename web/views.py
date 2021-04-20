from incidentes.models import Incidente
from django.shortcuts import render

# Create your views here.

def bienvenida (request):
    total_incidentes = Incidente.objects.count()
    incidentes = Incidente.objects.all()
    return render (request, "bienvenida.html", {"total": total_incidentes, "incidentes" : incidentes})