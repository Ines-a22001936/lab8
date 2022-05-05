from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import datetime


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
