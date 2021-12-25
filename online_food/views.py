from django.shortcuts import render


def home_page(request):
    return render(request, 'online_food/home.html')
