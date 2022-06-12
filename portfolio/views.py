# import matplotlib
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import datetime

from portfolio.forms import PostForm, CadeiraForm, ProjetoForm, TFCForm
from portfolio.models import *


# from matplotlib import pyplot as plt

# matplotlib.use('Agg')


def home_page_view(request):
    agora = datetime.datetime.now()

    context = {
        'hora': agora.hour,
    }

    return render(request, 'portfolio/home.html', context)


def login_page_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:degree'))
        else:
            return render(request, 'portfolio/aboutme.html', {
                'message': 'Credenciais Inválidas'
            })
    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Desconectado'
    })


def aboutme_page_view(request):
    context = {
        'cadeiras': Cadeira.objects.all(),
    }

    return render(request, 'portfolio/aboutme.html', context)


def projects_page_view(request):
    context = {
        'projetos': Projeto.objects.all(),
        'tfcs': TFC.objects.all()
    }

    return render(request, 'portfolio/projects.html', context)


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
        desenha_grafico_resultados()
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

    if request.POST['output2'] == '10, 11, 12, 13, 14, ':
        pontuacao += 1

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

    # plt.barh(nomes, pontuacoes)
    # plt.savefig('portfolio/static/portfolio/images/graficopontuacoes.png', bbox_inches="tight")


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')


@login_required
def novacadeira_page_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:degree'))

    context = {'form': form}

    return render(request, 'portfolio/novacadeira.html', context)


@login_required
def novoprojeto_page_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projects'))

    context = {'form': form}

    return render(request, 'portfolio/novoprojeto.html', context)


@login_required
def novotfc_page_view(request):
    form = TFCForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projects'))

    context = {'form': form}

    return render(request, 'portfolio/novotfc.html', context)


def web_page_view(request):
    context = {
        'tecnologias': Tecnologia.objects.all()
    }
    return render(request, 'portfolio/web.html', context)
