from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import HttpResponse

def home(request):
    return render(request, 'accueil/home.html')
