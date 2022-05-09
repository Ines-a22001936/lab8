from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import datetime

from django.urls import reverse

from .forms import PostForm
from .models import Post


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
