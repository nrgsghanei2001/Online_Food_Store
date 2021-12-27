from django.db import models
from django.db.models.base import Model
from accounts.models import *


class Category(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name}"


class Meal(models.Model):
    MEAL_CHOICES = (('bf', 'Break Fast'),
    ('ld', 'Lunch And Dinner'),
    ('sn', 'Snack'))

    meal = models.CharField(max_length=2, choices=MEAL_CHOICES, default='ld')


    def __str__(self):
        return f"{self.get_meal_display()}"


class Restaurant(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='branches')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="branch")
    menu = models.ManyToManyField('Menu', related_name='branches')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='branches')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='branches')
    details = models.TextField()
    date_of_register = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.restaurant}'\n'branch: {self.address}"


class Food(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    category = models.ManyToManyField(Category, related_name='foods')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
    date_of_record = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='foods/')


    def __str__(self):
        return self.name


class Menu(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='menus')
    price = models.FloatField()
    number_of_existance = models.PositiveIntegerField()


    def __str__(self) -> str:
        return f"food: {self.food}'\n'price: {self.price}'\n'number: {self.number_of_existance}"


class Order(models.Model):
    CUSTOMERS_STATUS = (('a', 'added'),
    ('c', 'confirmed'),
    ('s', 'is sending'),
    ('d', 'delivered'))

    RESTAURANT_STATUS = (('r', 'recorded'),
    ('p', 'in progress'),
    ('d', 'delivered'))

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='orders')
    menu = models.ManyToManyField(Menu, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders')
    order_time = models.DateTimeField(auto_now_add=True)
    customers_status = models.CharField(max_length=1, choices=CUSTOMERS_STATUS, default='a')
    restaurnat_status = models.CharField(max_length=1, choices=RESTAURANT_STATUS, default='r')

    def __str__(self):
        return f"{self.customer} {self.get_customers_status_display()}"


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    foods = models.ManyToManyField(Order, related_name='invoices')
    last_purchase = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.user.username
