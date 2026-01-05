from django.shortcuts import render

def logement(request):
    return render(request, 'logement/logement.html')