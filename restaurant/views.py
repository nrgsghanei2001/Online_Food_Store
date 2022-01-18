from django.shortcuts import render
from django.contrib import messages
from accounts.forms import RegisterForm
from online_food.urls import *
from .models import *
from django.contrib.auth.models import User
from .permissions import *


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
    perm = BranchOperations()
    if perm.has_perm_add_branch(request):
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
    
    else:
        return HttpResponseForbidden("This action is not supported!")


def edit(request):
    perm = BranchOperations()
    if perm.has_perm_for_edit(request):
        if request.method == 'POST' and request.is_ajax():
            text = request.POST
            print(text)
            item_id = text['name']
            item = MenuItem.objects.get(id=item_id)
            if text['price'] != "":
                price = float(text['price'])
                item.price = price
                item.save()
            if text['number'] != "":
                number = int(text['number'])
                item.number_of_existance = number
                item.save()
            return JsonResponse({})

        staff = Staff.objects.get(user=request.user)
        items = staff.restaurant.menu.item.all()
        context = {'items':items}
        return render(request, 'restaurant/edit_menu.html', context)
    else:
        return HttpResponseForbidden("This action is not supported!")


def show_menu(request):
    perm = BranchOperations()
    if perm.has_perm_for_menu_or_orders(request):
        if request.method == 'POST'  and request.is_ajax():
            text = request.POST
            action = text['action']
            if action == 'delete':
                menu_item = MenuItem.objects.get(id=text['item_id'])
                menu_item.delete()
                return JsonResponse({})

        staff = Staff.objects.get(user=request.user)
        try:
            menu = staff.restaurant.menu.item.all()
        except:
            menu = []
        context = {'menu':menu}
        return render(request, 'restaurant/show_menu.html', context)
    else:
        return HttpResponseForbidden("This page is not supported for non staff users!")


def add_to_menu(request):
    perm = BranchOperations()
    if perm.has_perm_for_menu_or_orders(request):
        if request.method == 'POST'  and request.is_ajax():
            text = request.POST
            print(text)
            food_id = text['food']
            food = Food.objects.get(id=food_id)
            price = float(text['price'])
            numner = int(text['number'])
            menu_item = MenuItem.objects.create(food=food, price=price, number_of_existance=numner)
            staff = Staff.objects.get(user=request.user)
            if not staff.restaurant.menu:
                menuc = Menu.objects.create()
                x = menuc.item.add(menu_item)
                staff.restaurant.menu.create(item=menu_item)
                staff.restaurant.save()
            else:
                menu = staff.restaurant.menu.item.add(menu_item)
                menu.save()

            return JsonResponse({})

        foods = Food.objects.all()
        context = {'foods':foods,}
        return render(request, 'restaurant/add_to_menu.html', context)
    else:
        return HttpResponseForbidden("This page is not supported for non staff users!")


def show_restaurants_orders(request):
    perm = BranchOperations()
    if perm.has_perm_for_menu_or_orders(request):
        staff = Staff.objects.get(user=request.user)
        branch = staff.restaurant
        orders = Order.objects.filter(restaurant=branch)
        context = {'orders':orders,}
        return render(request, 'restaurant/show_orders.html', context)
    else:
        return HttpResponseForbidden("This page is not supported for non staff users!")