from django.db import models

class User(models.Model):
    VENTANILLA = "VT"
    NOMINA = "NM"
    TYPE_ASOCIADOS = {
        VENTANILLA: "Ventanilla",
        NOMINA: "Nomina"
    }
    
    ONE = "Entre 0 y 2 años"
    TWO = "Entre 2 y 5 años"
    THREE = "Mayor a 5 años"
    TYPE_TIME = {
        ONE: "Entre 0 y 2 años",
        TWO: "Entre 2 y 5 años",
        THREE: "Mayor a 5 años"
    }
    
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    document = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_ASOCIADOS.items())
    time = models.CharField(max_length=20, choices=TYPE_TIME.items())

class DeudaAporte(models.Model):
    """"""
    name = models.CharField(max_length=100)
    tasa = models.FloatField()

class Extracupo(models.Model):
    """"""
    name = models.CharField(max_length=100)
    tasa = models.FloatField()