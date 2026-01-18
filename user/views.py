from django.shortcuts import render

def login(request):
    return render(request, 'user/login.html')
  
def register(request):
    return render(request, 'user/register.html')

def gesuser(request):
    return render(request, 'user/gesuser.html')

def create(request):
    return render(request, 'user/create.html')
