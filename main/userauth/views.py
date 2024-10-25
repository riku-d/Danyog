from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # This will raise an IntegrityError if the username already exists
                messages.success(request, 'Account created successfully!')
                return redirect('userauth:login')
            except IntegrityError:
                messages.error(request, 'An error occurred. Username might already exist.')
        else:
            messages.error(request, 'Form is invalid. Please correct the errors below.')
            # Log form errors for debugging
            for field in form:
                for error in field.errors:
                    print(f'Error in {field.name}: {error}')
            print(form.errors)  # This will print all errors to the console
    else:
        form = CustomUserCreationForm()

    return render(request, 'userauth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/')  # Replace 'home' with the correct redirect after login
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = CustomUserLoginForm()
    return render(request, 'userauth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')
