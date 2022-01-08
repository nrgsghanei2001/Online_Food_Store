from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, detail
from rest_framework import generics, viewsets, permissions, response, status
from rest_framework.views import APIView
from accounts.models import Customer
from online_food.models import *
from foods.models import *
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages


class AllFoods(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'foods/all_foods.html'

    def get(self, request):
        queryset = Food.objects.all()
        return Response({'object_list': queryset})


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
    return render(request, 'foods/add_food.html', context)


def add_category(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        print(text)
        category = Category.objects.create(name=text['name'])
        return JsonResponse({"text":text})
    return render(request, 'foods/add_category.html')


def delete_food(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        food = Food.objects.get(pk=text['food'])
        food.delete()
        return JsonResponse({})
    return JsonResponse({})


def edit(request, food_id=0, num=0):
    if num != 0:
        food = Food.objects.get(pk=food_id)
        name = food.name
        categories = Category.objects.all()
        context = {'categories' : categories}
        return render(request, 'foods/edit_food.html', context)

    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        name = text['name']
        detail = text['detail']
        category = text['category']
        meal = text['meal']
        image = text['image']
        food = Food.objects.get(name=name)
        if category != "":
            category = Category.objects.get(name=category)
            food.category.add(category)
        if meal != "":
            meal = Meal.objects.get(meal=meal)
            food.meal = meal
        if detail != "":
            food.detail = detail
        if food.image != "":
            food.image = image
        food.save()
        return JsonResponse({})


    return render(request, 'online_food/home.html')



def edit_food(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        # print(text)
        edit(request, text['food'], 1)
        return JsonResponse({})
    categories = Category.objects.all()
    meals = Meal.objects.all()
    context = {'categories' : categories,
    'meals' : meals,}
    return render(request, 'foods/edit_food.html' , context)