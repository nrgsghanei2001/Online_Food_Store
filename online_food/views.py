from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from accounts.models import Customer

from online_food.models import Branch, MenuItem, Order, OrderItem, Restaurant


def home_page(request):
    return render(request, 'online_food/home.html')


def add_food(request):
    return render(request, 'online_food/add_food.html')


class AllRestaurants(ListView):
    model = Branch
    template_name = 'online_food/all_restaurants.html' 


class RestaurantDetail(DetailView):
    model = Branch
    template_name = 'online_food/restaurants_detail.html' 


class Menu(DetailView):
    model = Branch
    template_name = 'online_food/restaurants_menu.html' 


def add_to_cart(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        menu_item=text.get('menu_item')
        menu_item = MenuItem.objects.get(id=menu_item)
        number=text.get('number')
        branch = menu_item.menus.get().branches
        price = int(number) * menu_item.price
        # print(price)
        customer = Customer.objects.get(user=request.user)
        flag = False 
        order_item = OrderItem.objects.create(item=menu_item, number=number, price=price)
        for obj in Order.objects.all():
            if obj.customer == customer:
                flag = True
                new_price = obj.total_price + price
                obj.menu.add(order_item)
                obj.total_price = new_price
                obj.save()
                print(obj.total_price)
                
        if not flag:
            order = Order.objects.create(customer=customer, restaurant=branch, total_price=price)
            order.menu.add(order_item)

        return JsonResponse({})

    return JsonResponse({})


class Cart(ListView):
    model = Order
    template_name = 'online_food/cart.html'