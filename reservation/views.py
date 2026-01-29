from django.shortcuts import render

# Create your views here.

def reservation(request):
     return render(request, 'reservation/reservation.html')

def homereservation(request):
    return render(request, 'reservation/homereservation.html')

def index(request):
    return render(request, 'reservation/index.html')

def create(request):
    return render(request, 'reservation/create.html')

def detail(request):
    return render(request, 'reservation/detail.html')

