from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from accounts.models import Customer

from online_food.models import Branch, Invoice, MenuItem, Order, OrderItem, Restaurant


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
            if obj.customer == customer and obj.customers_status == 'a':
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


def invoice(request):
    if request.method == 'POST'  and request.is_ajax():
        flag = False
        for order in Order.objects.all():
            if order.customer.user == request.user:
                for invoice in Invoice.objects.all():
                    if invoice.customer.user == request.user:
                        invoice.foods.add(order)
                        flag = True
                        order.customers_status = 'c'
                        order.save()
                        break;
                if not flag:
                    customer = Customer.objects.get(user=request.user)
                    new_invoice = Invoice.objects.create(customer=customer)
                    new_invoice.foods.add(order)
                    order.customers_status = 'c'
                    order.save()
                    break
        return JsonResponse({})

    return JsonResponse({})
