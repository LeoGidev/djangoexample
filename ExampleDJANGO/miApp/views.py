
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Dato
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    datos = Dato.objects.all()
    return render(request, 'dashboard.html', {'datos': datos})

def logout_view(request):
    logout(request)
    return redirect('login')

@user_passes_test(lambda u: u.is_superuser)
def dash2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('dashboard2')
    return render(request, 'dash2.html')

def agregar_dato(request):
    if request.method == "POST":
        dato = request.POST.get("dato")
        Fecha = timezone.now()
        print(f"Recibido dato: {dato}, Fecha: {Fecha}")  # Esto imprimirá en la consola
        # Guarda el dato en la base de datos
        nuevo_dato = Dato(Fecha=Fecha, dato=dato)
        #nuevo_dato.save()
        print("Dato guardado correctamente", nuevo_dato)  # Verifica si este mensaje se imprime
        return redirect('dashboard')  # Redirecciona a la página de dashboard después de agregar el dato
    return render(request, "dash2.html")



