from django.db import models

# Create your models here.

class Cafe(models.Model):
    nome = models.CharField(max_length=200)
    img = models.ImageField(upload_to="imagem_cafe")    
    local = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Passeio(models.Model):
    nome = models.CharField(max_length=200)
    img = models.ImageField(upload_to="imagem_passeio")
    local = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Praia(models.Model):
    nome = models.CharField(max_length=200)
    img = models.ImageField(upload_to="imagem_praia")
    local = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Jantar(models.Model):
    nome = models.CharField(max_length=200)
    img = models.ImageField(upload_to="imagem_jantar")
    local = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Bar(models.Model):
    nome = models.CharField(max_length=200)
    img = models.ImageField(upload_to="imagem_bar")
    local = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.nome

class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.IntegerField(default=0)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, blank=True)
    passeio = models.ForeignKey(Passeio, on_delete=models.CASCADE,blank=True)
    praia = models.ForeignKey(Praia, on_delete=models.CASCADE,blank=True)
    jantar = models.ForeignKey(Jantar, on_delete=models.CASCADE,blank=True)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.nome