from django.db import models


class Generos(models.Model):
  titulo = models.CharField(max_length=20)
  jogo_referencia = models.CharField(max_length=50,blank=True)
  habilidade_importante = models.CharField(max_length=50,blank=True)
  dentro_de_BTD6 = models.CharField(max_length=100,blank=True)

class Historia(models.Model):
  titulo = models.CharField(max_length=500)
  imagem = models.CharField(max_length=300)
  dica = models.CharField(max_length=200,blank=True)
  estilo = models.CharField(max_length=100,blank=True)
  autor = models.CharField(max_length=30,blank=True)

class Upgrade(models.Model):
  TIPOS_DE_DANO = [
    ("N/A","Normal"),
    ("Purple","Plasma"),
    ("Black","Explosão"),
    ("Purple, Lead","Energia"),
    ("Lead, Frozen","Afiado"),
    ("All","Passivo"),
  ]
  titulo = models.CharField(max_length=50)
  dano = models.IntegerField()
  tipo_de_dano = models.CharField(max_length=15, choices=TIPOS_DE_DANO)
  alcance = models.IntegerField()
  perfuracao = models.IntegerField()
  propriedades_especiais = models.CharField(max_length=100,blank=True)
