from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def home(request):
    return render(request, 'account/sign_up.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(request.POST)
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect('userhome')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/')


def log_out(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('/')


def sign_up(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        conf_pass = request.POST.get('confirm_password', '')

        user_check = User.objects.filter(username=username) | User.objects.filter(email=email)

        if user_check:
            messages.error(request, "This user name is already exists")
            return redirect('/')

        if password == conf_pass:
            user_obj = User.objects.create_user(first_name=name, password=password, email=email, username=username)
            print(user_obj)
            user_obj.save()

    return redirect('/')
