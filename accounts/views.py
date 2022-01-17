from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from restaurant.models import Staff
from .forms import RegisterForm
from online_food.urls import *
from .models import *
from django.contrib.auth.models import User
from .permissions import *


def SignupPageView(req):
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
            user2 = User.objects.get(username=user)
            customer = Customer.objects.create(user=user2)
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})


def profile(request):
    try:
        customer = Customer.objects.get(user=request.user)
        staff = 'no'
    except:
        customer = Staff.objects.get(user=request.user)
        print(customer.restaurant)
        staff = 'yes'
    context = {'customer':customer,
    'staff':staff,}
    return render(request, 'accounts/profile.html', context)


def edit_info(request):
    perm = EditInfo()
    if perm.has_perm(request):
        if request.method == 'POST'  and request.is_ajax():
            text = request.POST
            email = text['email']
            city = text['city']
            address1 = text['address']
            address = ""
            if city != "":
                address = Address.objects.create(city=city, address=address1)
            customer = Customer.objects.get(user=request.user)
            if email != "":
                customer.email = email
            if address != "":
                customer.address.add(address)
            customer.save()
            print(text)
            return JsonResponse({})

        customer = Customer.objects.get(user=request.user)
        context = {'customer':customer}
        return render(request, 'accounts/edit_info.html' , context)
    else:
        return HttpResponseForbidden("You are not allowed. please login as a customer!")


def remove_address(request):
    perm = EditInfo()
    if perm.has_perm(request):
        if request.method == 'POST'  and request.is_ajax():
            text = request.POST
            address1 = text['address_id']
            address = Address.objects.get(id=address1)
            address.delete()
            print(address)
            return JsonResponse({})

        return JsonResponse({})
    else:
        return HttpResponseForbidden("You are not allowed. please login as a customer!")

