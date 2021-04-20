from incidentes.forms import FormsIncidente, FormsPersona
from incidentes.models import Incidente, Persona
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory

# Create your views here.

def detalle_incidente(request, id : int):
    incidente = Incidente.objects.get(pk = id)
    return render (request, 'detalle.html', {'incidente': incidente})

def agregar_incidente(request):
    # FormsIncidente = modelform_factory(Incidente, exclude=[])
    if request.method == "POST":
        formaIncidente = FormsIncidente(request.POST)
        if formaIncidente.is_valid:
            formaIncidente.save()
            return redirect ("index")
    else:
        formaIncidente = FormsIncidente()
        
    return render (request, "agregar_incidente.html", {"form" : formaIncidente})

def editar_incidente(request, id : int):
    incidente = Incidente.objects.get(pk = id)
    if request.method == "POST":
        formaIncidente = FormsIncidente(request.POST,instance=incidente)
        if formaIncidente.is_valid:
            formaIncidente.save()
            return redirect ("index")
    else:
        formaIncidente = FormsIncidente(instance=incidente)
        
    return render (request, "editar_incidente.html", {"form" : formaIncidente})

def borrar_incidente(request, id : int):
    incidente = get_object_or_404(Incidente, pk=id)
    if incidente:
        incidente.delete()
    return redirect ("index")

def agregar_persona(request):
    # FormsPersona = modelform_factory(Persona, exclude=[])
    if request.method == "POST":
        formaPersona = FormsPersona(request.POST)
        if formaPersona.is_valid:
            formaPersona.save()
            return redirect ("index")
    else:
        formaPersona = FormsPersona()
        
    return render (request, "agregar_persona.html", {"form" : formaPersona})