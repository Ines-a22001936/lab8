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

class ProfessorTeorica(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    linkLusofona = models.URLField(blank=True)
    linkLinkedin = models.URLField(blank=True)

    def __str__(self):
        return self.nome[:50]


class ProfessorPratica(models.Model):
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
    docente_teorica = models.ForeignKey(ProfessorTeorica, on_delete=models.CASCADE, default="")
    docente_pratica = models.ForeignKey(ProfessorPratica, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.nome[:50]


class Projeto(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    cadeira = models.ManyToManyField(Cadeira, related_name='tem')
    imagem = models.ImageField(upload_to='static/portfolio/images')
    descricao = models.TextField()

    def __str__(self):
        return self.nome[:50]


class TFC(models.Model):
    titulo = models.CharField(max_length=50, primary_key=True)
    autor1 = models.CharField(max_length=50)
    autor2 = models.CharField(max_length=50)
    orientador = models.CharField(max_length=50)
    ano = models.IntegerField()
    resumo = models.TextField()
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='static/portfolio/images')

    def __str__(self):
        return self.titulo[:50]


class Tecnologia(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    criador = models.CharField(max_length=50)
    dataLancamento = models.CharField(max_length=50)
    descricao = models.TextField()
    link = models.URLField(blank=True)
    imagem = models.ImageField()

    def __str__(self):
        return self.nome[:50]
