from incidentes.forms import InfoFiltros
from incidentes.models import Incidente
from django.shortcuts import render

# Create your views here.

# def bienvenida (request):
#     total_incidentes = Incidente.objects.count()
#     incidentes = Incidente.objects.all()
#     return render (request, "bienvenida.html", {"total": total_incidentes, "incidentes" : incidentes, "form" : InfoFiltros()})


def bienvenida(request):
    incidentes = list(Incidente.objects.all())

    if request.method == "POST":
        form = InfoFiltros(request.POST)
        if form.is_valid:
            fecha_forms = str(form["fecha"].value())
            nom_empleado = form["nombre_empleado"].value()
            descripcion_forms = str(form["descripcion_incidente"].value())
            estatus = str(form["estatus"].value())

    else:
        form = InfoFiltros(request.POST)

    incidentes = devolver_lista_filtrada(incidentes, fecha_forms, nom_empleado, descripcion_forms, estatus)
    return render(request, "bienvenida.html", {"total": len(incidentes), "incidentes": incidentes, "form": form})


def is_not_blank(s):
    if s and s.strip():
        return True
    return False


def devolver_lista_filtrada(incidentes: list, fecha_forms, nom_empleado, descripcion_forms, estatus):
    filtrados = []
    for i in incidentes:
        fecha = str(i.fecha)
        if (is_not_blank(fecha) and fecha == fecha_forms):
            filtrados.append(i)

        rep_persona = str(i.reporto_persona)
        if (is_not_blank(rep_persona) and (i not in filtrados) and rep_persona.__contains__(nom_empleado)):
            filtrados.append(i)

        descripcion = str(i.descripcion)
        if (is_not_blank(descripcion) and (i not in filtrados) and descripcion.__contains__(descripcion_forms)):
            filtrados.append(i)

        if (not estatus or ((i not in filtrados) and estatus == str(i.estatus))):
            filtrados.append(i)

    return filtrados
