from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# render the login page
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login')
    return render(request, 'index.html')


@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return render(request, 'index.html')
