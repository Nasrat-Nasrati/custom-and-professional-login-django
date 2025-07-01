# accounts/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse

def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:home')  # اصلاح شده: اضافه کردن namespace
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('accounts:home')  # اصلاح شده: اضافه کردن namespace
    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url='accounts:login')
def home_view(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('accounts:login')


def contact_view(request):
    return HttpResponse("<h2>Welcome to the Contact Us page</h2>")

def services_view(request):
    return HttpResponse("<h2>Welcome to the Services page</h2>")

def news_view(request):
    return HttpResponse("<h2>Welcome to the News page</h2>")

@login_required(login_url='accounts:login')
def students_view(request):
    return HttpResponse("<h2>Welcome to the Students page (only for logged-in users)</h2>")

@login_required(login_url='accounts:login')
def teachers_view(request):
    return HttpResponse("<h2>Welcome to the Teachers page (only for logged-in users)</h2>")

@login_required(login_url='accounts:login')
def courses_view(request):
    return HttpResponse("<h2>Welcome to the Courses page (only for logged-in users)</h2>")
