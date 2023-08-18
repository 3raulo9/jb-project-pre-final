from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomSignUpForm 
from .models import Record


def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome")
            return redirect('home')
        else:
            messages.success(request, "there appears to be an error, please check your details")
            return redirect('home')
    else:    
        return render(request, 'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "Register success")
            return redirect('home')
    else:
        form = CustomSignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})
