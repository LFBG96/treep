from django.db import models
from django.contrib.auth.models import User

from datetime import date


# Create your models here.

class Natureza(models.Model):
    nome = models.CharField(max_length=200)
    descricão = models.TextField(max_length=500)
    img = models.ImageField(upload_to="imagem_natureza")    
    cidade = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Gastronomia(models.Model):
    nome = models.CharField(max_length=200)
    descricão = models.TextField(max_length=500)
    img = models.ImageField(upload_to="imagem_gastronomia")
    cidade = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Praia(models.Model):
    nome = models.CharField(max_length=200)
    descricão = models.TextField(max_length=500)
    img = models.ImageField(upload_to="imagem_praia")
    cidade = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Cultura(models.Model):
    nome = models.CharField(max_length=200)
    descricão = models.TextField(max_length=500)
    img = models.ImageField(upload_to="imagem_cultura")
    cidade = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome



class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(default=date.today())
    natureza = models.ManyToManyField(Natureza, blank=True)    
    gastronomia = models.ManyToManyField(Gastronomia, blank=True)    
    praia = models.ManyToManyField(Praia,blank=True)    
    cultura = models.ManyToManyField(Cultura,blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
