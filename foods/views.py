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