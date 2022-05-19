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
    pontuacao = models.TextField()

    def __str__(self):
        return self.nome[:50]


# DER
class Projeto(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    imagem = models.ImageField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome[:50]


class Professor(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    linkLusofona = models.URLField(blank=True)
    linkLinkedin = models.URLField(blank=True)
    projetos_fk = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    projetos = models.ManyToManyField(Projeto, related_name='apoia')

    def __str__(self):
        return self.nome[:50]


class Cadeira(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    ranking = models.IntegerField()
    ano = models.IntegerField()
    topicos = models.TextField()
    etcs = models.IntegerField()
    docente_fk = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docente = models.ManyToManyField(Professor, related_name='leciona')
    projetos = models.ManyToManyField(Projeto, related_name='tem')

    def __str__(self):
        return self.nome[:50]

