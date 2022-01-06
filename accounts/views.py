from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
# from .forms import CustomUserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from online_food.urls import *


def SignupPageView(req):
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy('login')
    return render(req, 'registration/signup.html')

def register(request):
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
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})