from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error = None
    username_value = ''
    if request.method == 'POST':
        username_value = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username_value, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:home')
        error = 'Invalid username or password. Please try again.'

    context = {
        'error': error,
        'username': username_value,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
