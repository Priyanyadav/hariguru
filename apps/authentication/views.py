# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from apps.home.models import employee


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                return redirect("home")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def emplogin_view(request):
    form = {}
    msg = ""
    if request.method == 'POST':
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        form = {"email":em,
                "password":pwd
                }
        chkeml = employee.objects.filter(email=em)

        if chkeml.exists():
            if chkeml[0].password == pwd:
                request.session['id'] = chkeml[0].id 
                request.session['ename'] = chkeml[0].ename
                request.session['email'] = chkeml[0].email
                msg ="Successful Logged In"
                return redirect("home")
            else:
                msg = "Wrong Password"
        else:
            msg = "Invalid credentials, please try again"

    return render(request, 'accounts/loginn.html', {"form": form, "msg": msg})  

def empregister_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def logout(request):
    if 'id' in request.session:
        del request.session['id']
        del request.session['ename'] 
        del request.session['email']
        return redirect('loginn')