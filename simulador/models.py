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
    name = models.CharField(max_length=100, unique=True)
    tasa = models.FloatField()
    montoMax = models.IntegerField()
    plazoMin = models.IntegerField()
    plazoMax = models.IntegerField()
    garantia = models.TextField(max_length=500)
    requisitos = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.name} entre {self.plazoMin} y {self.plazoMax} cuotas"


class Extracupo(models.Model):
    """"""
    name = models.CharField(max_length=100)
    tasa = models.FloatField()
    montoMax = models.IntegerField()
    plazoMin = models.IntegerField()
    plazoMax = models.IntegerField()
    garantia = models.CharField(max_length=500)
    requisitos = models.CharField(max_length=500)
    
class Simulation(models.Model):
    name =models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    others = models.CharField(max_length=100)
    debit = models.CharField(max_length=100)
    typeCredit = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    cuotas = models.CharField(max_length=100)

class Salary(models.Model):
    """"""
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)