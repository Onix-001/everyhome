from django.shortcuts import render

def logement(request):
    return render(request, 'logement/logement.html')

def index(request):
    return render(request, 'logement/index.html')

def create(request):
    return render(request, 'logement/create.html')