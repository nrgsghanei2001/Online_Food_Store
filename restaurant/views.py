from django.shortcuts import render
from django.contrib import messages
from accounts.forms import RegisterForm
from online_food.urls import *
from .models import *
from django.contrib.auth.models import User


def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'accounts/register_staff.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # print(email)
            user2 = User.objects.get(username=user)
            Staff.objects.create(user=user2, email=email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'accounts/register_staff.html', context)

    return render(request, 'accounts/register_staff.html', {})


def add_branch(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        restaurant = Restaurant.objects.get(id=text['restaurant'])
        city = text['city']
        address = text['address']
        address1 = Address.objects.create(city=city, address=address)
        category = text['category']
        category1 = Category.objects.create(name=category)
        meal = Meal.objects.get(id=text['meal'])
        details = text['details']
        branch = Branch.objects.create(restaurant=restaurant, address=address1, category=category1, meal=meal, details=details)
        staff = Staff.objects.get(user=request.user)
        staff.restaurant = branch
        staff.save()
        return JsonResponse({})

    meals = Meal.objects.all()
    restaurants = Restaurant.objects.all()
    context = {'meals':meals,
    'restaurants':restaurants,}
    return render(request, 'accounts/add_branch.html', context)


def show_menu(request):
    staff = Staff.objects.get(user=request.user)
    menu = staff.restaurant.menu.item.all()
    context = {'menu':menu}
    return render(request, 'restaurant/show_menu.html', context)

