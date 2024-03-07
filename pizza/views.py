from django.shortcuts import render, redirect
from .models import Pizza, Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
@@ -10,3 +12,38 @@ def home(request):
    }

    return render(request, 'home.html', context=context)


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, template_name='register.html', context={'error': 'Username already exists'})
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')

    return render(request, template_name='register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name='login.html', context={'error': 'Invalid username or password'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')