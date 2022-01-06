from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, detail
from rest_framework import generics, viewsets, permissions, response, status
from rest_framework.views import APIView
from accounts.models import Customer
from .serializers import *
from online_food.models import Branch, Food, Invoice, MenuItem, Order, OrderItem, Restaurant
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


def home_page(request):
    return render(request, 'online_food/home.html')


def add_food(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        name = text['name']
        detail = text['detail']
        category = text['category']
        category = Category.objects.get(name=category)
        meal = text['meal']
        meal = Meal.objects.get(meal=meal)
        image = text['image']
        food = Food.objects.create(name=name, detail=detail, meal=meal, image=image)
        food.category.add(category)
        food.save()
        return JsonResponse({"text":text})
    
    categories = Category.objects.all()
    meals = Meal.objects.all()
    context = {'categories' : categories, 
    'meals' : meals}
    return render(request, 'online_food/add_food.html', context)


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
        branch = menu_item.menus.last().branches
        price = int(number) * menu_item.price
        # print(price)
        try:
            customer = Customer.objects.get(user=request.user)
        except:
            device = request.COOKIES['device']
            try:
                customer = Customer.objects.get(device=device)
            except:
                customer = Customer.objects.create(device=device)
            print(customer)
        flag = False 
        order_item = OrderItem.objects.create(item=menu_item, number=number, price=price)
        for obj in Order.objects.all():
            if obj.customer == customer and obj.customers_status == 'a' and obj.restaurant == branch:
                flag = True
                new_price = obj.total_price + price
                obj.menu.add(order_item)
                obj.total_price = new_price
                obj.save()
                # print(obj.total_price)
            elif obj.restaurant != branch:
                obj.delete()
                
        if not flag:
            print("ding")
            print(type(customer))
            order = Order.objects.create(customer=customer, restaurant=branch, total_price=price)
            order.menu.add(order_item)

        return JsonResponse({})

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

# class Cart(ListView):
#     model = Order
#     template_name = 'online_food/cart.html'


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


class AllFoods(APIView):
    # serializer_class = FoodSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'online_food/all_foods.html'

    def get(self, request):
        queryset = Food.objects.all()
        return Response({'object_list': queryset})

    # def post(self, request):
    #     food = get_object_or_404(Food)
    #     serializer = FoodSerializer(food, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'object_list': food})
    #     serializer.save()
    #     return redirect('food-list')

    # queryset = Food.objects.all()
    # model = Food
    # template_name = 'online_food/add_food_admin.html'



# class PopularFoods(ListView):
#     model = Invoice
#     template_name = 'online_food/popular_foods.html'

#     def get_queryset(self):
#         all_invoices = Invoice.objects.all()
#         for invoice in all_invoices:
#             orders = invoice.foods.all()
#             for order in orders:
#                 order_items = order.menu.all()

#         return query_set


