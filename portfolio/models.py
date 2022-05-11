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
