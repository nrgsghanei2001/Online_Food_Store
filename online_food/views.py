from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from online_food.models import Branch


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