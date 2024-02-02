from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import userProfile


def register(request):
    if request.user.is_authenticated:
        return redirect("hello")
    if request.method == 'POST':
        print("hello")
        first_name=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        user = User.objects.create_user(
                username = first_name,
                password = password,
                email = email,
            )
        return redirect("user_auth:login")
    else:
        return render(request, "user_auth/register.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("auth_user:home")
    
    if request.POST:
        print("login point")
        username = request.POST.get('uname')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('logged in')
            return redirect("auth_user:home")
        else:
            return render(request, "user_auth/login.html", {'error_message' : 'Enter Valid credentials' })
    else:
        return render(request, "user_auth/login.html")

def logout(req):
    logout(req)
    return render(req, "user_auth/home.html")
    


# def auth_login(request):

# def auth_logout(request):
    


