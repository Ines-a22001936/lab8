"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view),
    path('home', views.home_page_view, name='home'),
    path('aboutme', views.aboutme_page_view, name='aboutme'),
    path('projects', views.projects_page_view, name='projects'),
    path('blog', views.blog_page_view, name='blog'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('contact', views.contact_page_view, name='contact'),
    path('novacadeira', views.novacadeira_page_view, name='novacadeira'),
    path('novoprojeto', views.novoprojeto_page_view, name='novoprojeto'),
    path('novotfc', views.novotfc_page_view, name='novotfc'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('web', views.web_page_view, name='web'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
