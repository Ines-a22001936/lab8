from django.db import models


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    autor = models.CharField(max_length=100)
    criado = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome[:50]


# DER

class Professor(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    linkLusofona = models.URLField(blank=True)
    linkLinkedin = models.URLField(blank=True)

    def __str__(self):
        return self.nome[:50]


class Cadeira(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    ranking = models.IntegerField()
    ano = models.IntegerField()
    topicos = models.TextField()
    etcs = models.IntegerField()
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='apoia')

    def __str__(self):
        return self.nome[:50]


class Projeto(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    cadeira = models.ManyToManyField(Cadeira, related_name='tem')
    imagem = models.ImageField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome[:50]
