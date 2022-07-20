from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        context = {}
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            print(password)
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Wrong credentials given")

        return render(request, template_name='login.html', context=context)

def logout_user(request):
    logout(request)
    messages.error(request, '')
    return redirect('/auth/login')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            user = authenticate(request,username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                return redirect('/')
            # return redirect('/')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})
