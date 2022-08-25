from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def register(request):
    #GET
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully registered...')
            return redirect('/profile/')
    context = {
        'form':form
    }
    return render(
        request,
        'account/register.html',
        context
    )
    #POST

def log_in(request):
    #GET
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_logued = authenticate(username = username, password = password)
            if user_logued is not None:
                messages.add_message(request, messages.SUCCESS, 'Welcome {}'.format(user_logued.get_username()))
                login(request, user_logued)
                return redirect('/profile/')
    context = {
        'form':form
    }
    return render(
        request, 
        'account/login.html',
        context
    )
    #POST

def log_out(request):
    logout(request)
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        return render(
            request,
            'account/profile.html'
        )
    return redirect('/profile')