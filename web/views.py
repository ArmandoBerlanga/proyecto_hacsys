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
    copia = []
    for i in incidentes:
        copia.append(i)

    if request.method == "POST":
        form = InfoFiltros(request.POST)
        if form.is_valid:
            fecha_forms = str(form["fecha"].value())
            nom_empleado = str(form["nombre_empleado"].value())
            descripcion_forms = str(form["descripcion_incidente"].value())
            estatus = str(form["estatus"].value())

            for i in incidentes:
                if not ((fecha_forms == str(i.fecha) or not fecha_forms) and nom_empleado in str(i.reporto_persona) and
                descripcion_forms in str(i.descripcion) and (estatus == str(i.estatus) or not estatus)):
                    copia.remove(i) 
    else:
        form = InfoFiltros(request.POST)

    salida = False
    if copia:
        salida = True 
    else:
        copia = incidentes
    return render(request, "bienvenida.html", {"total": len(copia), "incidentes": copia, "form": form, "salida" : salida})