from incidentes.forms import InfoFiltros
from incidentes.models import Incidente
from django.shortcuts import render

# Create your views here.

# def bienvenida (request):
#     total_incidentes = Incidente.objects.count()
#     incidentes = Incidente.objects.all()
#     return render (request, "bienvenida.html", {"total": total_incidentes, "incidentes" : incidentes, "form" : InfoFiltros()})


def bienvenida(request):
    incidentes = list(Incidente.objects.all()) # se obtiene una lista de los objetos incidente
    copia = [] # se hace una copia para su manipulacion direct
    for i in incidentes: # se agregan a la copia c/u
        copia.append(i)

    # PARA LA FUNCION DE FILTRO
    if request.method == "POST": # si el metodo de entrega de datos es POST
        form = InfoFiltros(request.POST) # creo un forms y pido la info al usuario
        if form.is_valid: # si la info es valida lo paso, si no no
            fecha_forms = str(form["fecha"].value()) # recupera la informacion
            nom_empleado = str(form["nombre_empleado"].value())
            descripcion_forms = str(form["descripcion_incidente"].value())
            estatus = str(form["estatus"].value())

            for i in incidentes: # para cada inicidente evaluo si sea mostrado o no
                if not ((fecha_forms == str(i.fecha) or not fecha_forms) and nom_empleado in str(i.reporto_persona) and
                descripcion_forms in str(i.descripcion) and (estatus == str(i.estatus) or not estatus)):
                    copia.remove(i) # si no cumple lo remuevo de la lista
    else:
        form = InfoFiltros(request.POST) # si no es post, sera por primera vez y creo un forms nuevo

    salida = False # var de mensaje dentro de html, si se encontro en el filtro o no
    if copia:
        salida = True 
    else:
        copia = incidentes
    return render(request, "bienvenida.html", {"total": len(copia), "incidentes": copia, "form": form, "salida" : salida})