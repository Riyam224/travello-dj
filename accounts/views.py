from django.shortcuts import render , redirect

# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate , login, logout
from .forms import RegisterForm



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'you create account ')
            return redirect('/')
    else:
        form = RegisterForm()
    

    return render(request , 'accounts/register.html' , {'form': form})