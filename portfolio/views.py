from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import datetime

from django.urls import reverse

from .forms import PostForm
from .models import Post, PontuacaoQuizz
from matplotlib import pyplot as plt


def home_page_view(request):
    agora = datetime.datetime.now()

    context = {
        'hora': agora.hour,
    }

    return render(request, 'portfolio/home.html', context)


def degree_page_view(request):
    return render(request, 'portfolio/degree.html')


def projects_page_view(request):
    return render(request, 'portfolio/projects.html')


def skills_page_view(request):
    skills = ['none', 'quick problem solving', 'play the piano', 'i like to eat 4 donuts a day (should be a skill)']

    context = {
        'skills': skills,
    }

    return render(request, 'portfolio/skills.html', context)


def blog_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {
        'posts': Post.objects.all(),
        'form': form
    }
    return render(request, 'portfolio/blog.html', context)


def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    return render(request, 'portfolio/quizz.html')


def pontuacao_quizz(request):
    pontuacao = 0

    if request.POST['language'] == 'python':
        pontuacao += 1

    if request.POST.get('html') == 'hypertext':
        pontuacao += 1

    if request.POST['doctype'] == 'false':
        pontuacao += 1

    if request.POST['output1'] == 'maJ':
        pontuacao += 1

    if request.POST['init'] == 'package':
        pontuacao += 1

    if request.POST.get('format') == 'pixels':
        pontuacao += 1

    if request.POST['defined'] == 'false2':
        pontuacao += 1

    if request.POST['output2'] == '10, 11, 12, 13, 14,':
        pontuacao += 1

    desenha_grafico_resultados()
    return pontuacao


def desenha_grafico_resultados():
    users = sorted(PontuacaoQuizz.objects.all(), key=lambda x: x.pontuacao)
    nomes = []
    pontuacoes = []

    for user in users:
        nomes.append(user.nome)
        pontuacoes.append(user.pontuacao)

    nomes.reverse()
    pontuacoes.reverse()

    plt.barh(nomes, pontuacoes)
    plt.savefig('graficopontuacoes.png', bbox_inches="tight")


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')
