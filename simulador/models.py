from django.db import models

class SocialesRetencion(models.Model):
    """"""
    name = models.CharField(max_length=100, unique=True)
    rango1 = models.CharField(max_length=200)
    rango2 = models.CharField(max_length=200)
    rango3 = models.CharField(max_length=200)
    rango4 = models.CharField(max_length=200)
    rango5 = models.CharField(max_length=200)
    rango6 = models.CharField(max_length=200)
    rango7 = models.CharField(max_length=200)    
    aportesMax = models.IntegerField()
    plazoMax = models.IntegerField()
    garantia = models.TextField(max_length=500)
    requisitos = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.name} aportes maximos {self.plazoMax}"

class Sociales(models.Model):
    """"""
    name = models.CharField(max_length=100, unique=True)
    rango1 = models.CharField(max_length=200)
    rango2 = models.CharField(max_length=200)
    rango3 = models.CharField(max_length=200)
    rango4 = models.CharField(max_length=200, null=True, blank=True)
    rango5 = models.CharField(max_length=200, null=True, blank=True)
    rango6 = models.CharField(max_length=200, null=True, blank=True)
    rango7 = models.CharField(max_length=200, null=True, blank=True)  
    rango8 = models.CharField(max_length=200, null=True, blank=True)
    plazoMax = models.IntegerField()
    garantia = models.TextField(max_length=500)
    requisitos = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} aportes maximos {self.plazoMax}"

class Extra(models.Model):
    """"""
    name = models.CharField(max_length=100, unique=True)
    plazoMax = models.IntegerField()
    garantia = models.TextField(max_length=500)
    requisitos = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.name}"

class Tasas(models.Model):
    name = models.CharField(max_length=100)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    fianza = models.FloatField()
    plazoMax = models.IntegerField()
    garantia = models.TextField(max_length=500, default=None, null=True)
    requsitos = models.TextField(max_length=500, default=None, null=True)
    tasa = models.FloatField()
    
    def __str__(self):
        return f"{self.name} socre {self.scoreMax} - {self.scoreMin}: tasa {self.tasa}"

class Salary(models.Model):
    """"""
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

# class DeudaAporte(models.Model):
#     """"""
#     name = models.CharField(max_length=100, unique=True)
#     tasa = models.FloatField()
#     montoMax = models.IntegerField()
#     plazoMin = models.IntegerField()
#     plazoMax = models.IntegerField()
#     garantia = models.TextField(max_length=500)
#     requisitos = models.TextField(max_length=500)
    
#     def __str__(self):
#         return f"{self.name} entre {self.plazoMin} y {self.plazoMax} cuotas"

# class Extracupo(models.Model):
#     """"""
#     name = models.CharField(max_length=100, unique=True)
#     tasa = models.FloatField()
#     montoMax = models.IntegerField()
#     plazoMin = models.IntegerField()
#     plazoMax = models.IntegerField()
#     garantia = models.TextField(max_length=2000)
#     requisitos = models.TextField(max_length=2000)
    
#     def __str__(self):
#         return f"{self.name}"
    
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

