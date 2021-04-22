from incidentes.forms import FormsAcccion, FormsIncidente, FormsPersona
from incidentes.models import Accion, Incidente, Persona
from django.shortcuts import get_object_or_404, redirect, render


def detalle_incidente(request, id: int):  # para desplegar info de un incidente
    incidente = Incidente.objects.get(pk=id)  # obtengo el incidente
    # obtengo las acciones que tengan el mismo id, son n
    acciones = Accion.objects.filter(id_conexion=id)
    acciones = list(acciones)
    return render(request, 'detalle.html', {'incidente': incidente, "lista_acciones": acciones})


def agregar_incidente(request):  # creacion de un forms para agregar incidente
    if request.method == "POST":
        formaIncidente = FormsIncidente(request.POST)
        if formaIncidente.is_valid:
            formaIncidente.save()
            return redirect("index")
    else:
        formaIncidente = FormsIncidente()

    return render(request, "agregar_incidente.html", {"form": formaIncidente})


def editar_incidente(request, id: int):  # creacion de un forms para editar incidente
    incidente = Incidente.objects.get(pk=id)
    if request.method == "POST":
        formaIncidente = FormsIncidente(request.POST, instance=incidente)
        if formaIncidente.is_valid:
            # si el estatus cambia respecto al original
            # if formaIncidente['estatus'].value() != incidente.estatus:
            # code para el cambio de estatus con razon de cambio requerida
            formaIncidente.save()
            return redirect("index")
    else:
        formaIncidente = FormsIncidente(instance=incidente)

    return render(request, "editar_incidente.html", {"form" : formaIncidente})


def borrar_incidente(request, id: int):  # para borrar un incidente
    incidente = get_object_or_404(Incidente, pk=id)  # lo obtengo
    if incidente:  # veo que sea valido
        incidente.delete()  # lo borro
    return redirect("index")


# el compartamiento de los demas objetos es similar, funciona con accion y persona
def agregar_persona(request):
    if request.method == "POST":
        formaPersona = FormsPersona(request.POST)
        if formaPersona.is_valid:
            formaPersona.save()
            return redirect("index")
    else:
        formaPersona = FormsPersona()

    return render(request, "agregar_persona.html", {"form": formaPersona})


def agregar_accion(request, id: int):
    if request.method == "POST":
        formsAccion = FormsAcccion(request.POST)
        if formsAccion.is_valid:
            formsAccion.save()
            return redirect(f"http://127.0.0.1:8000/detalle_incidente_{id}")
    else:
        formsAccion = FormsAcccion()

    return render(request, "agregar_acciones.html", {"form": formsAccion})

def editar_accion(request, id_con: int, id: int):
    accion = Accion.objects.get(pk=id_con)
    if request.method == "POST":
        formsAccion = FormsAcccion(request.POST, instance=accion)
        if formsAccion.is_valid:
            formsAccion.save()
            return redirect(f"http://127.0.0.1:8000/detalle_incidente_{id}")
    else:
        formsAccion = FormsAcccion(instance=accion)

    return render(request, "editar_acciones.html", {"form": formsAccion})


def borrar_accion(request, id_con: int, id: int):
    accion = get_object_or_404(Accion, pk=id_con)
    if accion:
        accion.delete()
    return redirect(f"http://127.0.0.1:8000/detalle_incidente_{id}")
