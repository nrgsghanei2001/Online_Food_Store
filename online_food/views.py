from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, detail
from rest_framework import generics, viewsets, permissions, response, status
from rest_framework.views import APIView
from accounts.models import Customer
from .serializers import *
from online_food.models import *
from foods.models import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages


def home_page(request):
    queryset = MenuItem.objects.filter().order_by('-order_time')[:3]
    queryset2 = Branch.objects.filter().order_by('-order_time')[:3]
    context = {'populars' : queryset,
    'pop_res': queryset2}
    return render(request, 'online_food/home.html' , context)


def admin_page(request):
    return render(request, 'online_food/admin.html')


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
        if int(number) <= menu_item.number_of_existance:
            menu_item.order_time += int(number)
            menu_item.number_of_existance -= int(number)
            menu_item.save()
            branch = menu_item.menus.last().branches
            branch.order_time += int(number)
            branch.save()
            price = int(number) * menu_item.price
            try:
                customer = Customer.objects.get(user=request.user)
            except:
                device = request.COOKIES['device']
                try:
                    customer = Customer.objects.get(device=device)
                except:
                    customer = Customer.objects.create(device=device)
            flag = False 
            order_item = OrderItem.objects.create(item=menu_item, number=number, price=price)
            for obj in Order.objects.all():
                if obj.customer == customer and obj.customers_status == 'a' and obj.restaurant == branch:
                    flag = True
                    new_price = obj.total_price + price
                    obj.menu.add(order_item)
                    obj.total_price = new_price
                    obj.save()
                elif obj.restaurant != branch:
                    obj.delete()
                    
            if not flag:
                order = Order.objects.create(customer=customer, restaurant=branch, total_price=price)
                order.menu.add(order_item)

            return JsonResponse({})
        else:
            context = {'error':"There is not exist this much of the food you chose!"}
            return render(request, 'online_food/restaurants_menu.html', context)

    return JsonResponse({})

def cart(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except:
        device = request.COOKIES['device']
        customer = Customer.objects.get(device=device)
    order = Order.objects.filter(customer=customer)
    context = {'order': order}
    return render(request, 'online_food/cart.html', context)


def invoice(request):
    print("dang")
    if request.method == 'POST'  and request.is_ajax():
        flag = False
        print(request.POST)
        for order in Order.objects.all():
            if order.customer.user == request.user:
                for invoice in Invoice.objects.all():
                    if invoice.customer.user == request.user:
                        invoice.foods.add(order)
                        flag = True
                        order.customers_status = 'c'
                        order.total_price = 0
                        order.save()
                        break;
                if not flag:
                    customer = Customer.objects.get(user=request.user)
                    new_invoice = Invoice.objects.create(customer=customer)
                    new_invoice.foods.add(order)
                    order.customers_status = 'c'
                    order.total_price = 0
                    order.save()
                    break
        return JsonResponse({})

    return JsonResponse({})


def delete_item(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        order_item = OrderItem.objects.get(pk=text['order_item'])
        order = order_item.orders.last()
        order.total_price -= order_item.price
        order_item.delete()
        order.save()
        return render(request, 'online_food/cart.html')
    return render(request, 'online_food/cart.html')




