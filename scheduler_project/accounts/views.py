# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.http import HttpResponseBadRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):

    if request.user.is_authenticated:

        return redirect('scheduler:index_schedule')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()    
            login(request, user)  
            return redirect('scheduler:index_schedule')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def signin(request):

    if request.user.is_authenticated:   

        return redirect('scheduler:index_schedule')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
        
            user = form.get_user()  
            login(request, user)   
         
            return redirect(request.GET.get('next') or 'scheduler:index_schedule')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {
        'form': form,
    })


def signout(request):
    logout(request)
    return redirect('scheduler:index_schedule')