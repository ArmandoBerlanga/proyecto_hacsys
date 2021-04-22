from django.db import models


class Persona (models.Model):
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido_materno} {self.apellido_materno}"

class Incidente (models.Model):
    reporto_persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    estatus = models.BooleanField()
    razon_de_cambio = models.CharField(max_length=255)

    def __str__(self):
        return f"ID [{self.id}] {self.descripcion} || {self.fecha}"

class Accion (models.Model):
    id_conexion = models.ForeignKey(Incidente, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"[{self.id_conexion}] {self.descripcion}"