from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import UserProfile
from django.views.decorators.csrf import csrf_protect

# Page de connexion
def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        # Authentification : essayer par username, sinon email
        user = authenticate(request, username=username_or_email, password=password)
        if not user:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            auth_login(request, user)
            messages.success(request, f"Bienvenue {user.first_name} !")
            return redirect("accueil:home")  # rediriger vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur/email ou mot de passe incorrect.")

    return render(request, "user/login.html")


# Page d'inscription
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Vérifier que les mots de passe correspondent
        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("register")

        # Vérifier si username ou email existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return redirect("register")

        # Créer l'utilisateur
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password1
        )

        # Créer le profil avec téléphone
        UserProfile.objects.create(user=user, phone_number=phone_number)

        messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
        return redirect("account:login")

    return render(request, "user/register.html")


# Déconnexion
def logout_view(request):
    auth_logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect("account:login")
