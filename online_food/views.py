from django.db import models
from django.http import JsonResponse
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, TemplateView, detail
from rest_framework import generics, viewsets, permissions, response, status
from rest_framework.views import APIView
from accounts.models import Customer
from restaurant.models import Staff
from .serializers import *
from online_food.models import *
from foods.models import *



def home_page(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST.get('name')
        print(text)
        # search(request, text)
        p = list(MenuItem.objects.filter(food__name=text))
        counter = 1
        context = {}
        for i in p:
            y = str(i.food.image)
            x = {'name':i.food.name, 'price':i.price, 'link': i.menus.last().branches.id, 'img': y}
            key = str(counter)
            context[key] = x
            counter += 1

        return JsonResponse(context)

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
                    break;
                elif obj.customer == customer and obj.customers_status == 'a' and obj.restaurant != branch:
                    obj.delete()
                    break;
                elif obj.customer == customer and obj.customers_status != 'a':
                    flag = True
                    order = Order.objects.create(customer=customer, restaurant=branch, total_price=price)
                    order.menu.add(order_item)
                    break;
                    
            if not flag:
                order = Order.objects.create(customer=customer, restaurant=branch, total_price=price)
                order.menu.add(order_item)

            return JsonResponse({})
        else:
            context = {'error':"There is not exist this much of the food you chose!"}
            return render(request, 'online_food/restaurants_menu.html', context)

    return JsonResponse({})

def cart(request):
    device = request.COOKIES['device']
    try:
        try:
            customer = Customer.objects.get(user=request.user)
            staff = "no"
            try:
                cutomer2 = Customer.objects.get(device=device)
                try:
                    order2 = Order.objects.get(customer=cutomer2)
                    order2.customer = customer
                    order2.save()
                    cutomer2.delete()
                except:
                    cutomer2.delete()
            except:
                pass
        except:
            customer = Staff.objects.get(user=request.user)
            staff = "yes"
    except:
        try:
            customer = Customer.objects.get(device=device)
        except:
            customer = Customer.objects.create(device=device)
        staff = "no"
    if staff == 'no':
        order = Order.objects.filter(customer=customer)
    else:
        order = []
    context = {'order': order,
    'customer':customer,
    'staff':staff}
    return render(request, 'online_food/cart.html', context)


def invoice(request):
    if request.method == 'POST'  and request.is_ajax():
        flag = False
        text = request.POST
        address_id = text['address']
        address = Address.objects.get(id=address_id)
        for order in Order.objects.all():
            if order.customer.user == request.user:
                for invoice in Invoice.objects.all():
                    if invoice.customer.user == request.user:
                        order.address = address
                        order.save()
                        invoice.foods.add(order)
                        flag = True
                        order.customers_status = 'c'
                        order.total_price = 0
                        order.save()
                        break;
                if not flag:
                    customer = Customer.objects.get(user=request.user)
                    new_invoice = Invoice.objects.create(customer=customer)
                    order.address = address
                    order.save()
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


def all_orders(request):
    try:
        customer = Customer.objects.get(user=request.user)
        confirmed_orders = Order.objects.filter(customers_status='c', customer=customer)
        is_sending_orders = Order.objects.filter(customers_status='s', customer=customer)
        delivered_orders = Order.objects.filter(customers_status='d', customer=customer)
        context = {
            'confirmed_orders':confirmed_orders,
            'is_sending_orders':is_sending_orders,
            'delivered_orders':delivered_orders,
        }
        return render(request, 'online_food/all_orders.html', context)
    except:
        return HttpResponseForbidden("This page is not supperted for staffs")



