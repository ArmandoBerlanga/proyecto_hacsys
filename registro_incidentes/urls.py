"""registro_incidentes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from incidentes.views import agregar_incidente, agregar_persona, borrar_incidente, detalle_incidente, editar_incidente
from django.contrib import admin
from django.urls import path
from web.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida, name="index"),
    path("detalle_incidente_<int:id>/", detalle_incidente),
    path("editar_incidente_<int:id>/", editar_incidente),
    path("borrar_incidente_<int:id>/", borrar_incidente),
    path("agregar_incidente/", agregar_incidente),
    path("agregar_persona/", agregar_persona),
]
