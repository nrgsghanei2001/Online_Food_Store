from django.db import models
from django.db.models.base import Model
from accounts.models import *
import jdatetime


class Category(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name}"


class Meal(models.Model):
    MEAL_CHOICES = (('Break Fast', 'Break Fast'),
    ('Lunch And Dinner', 'Lunch And Dinner'),
    ('Snack', 'Snack'))

    meal = models.CharField(max_length=20, choices=MEAL_CHOICES, default='Lunch And Dinner')


    def __str__(self):
        return f"{self.get_meal_display()}"


class Restaurant(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='branches')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="branch")
    menu = models.OneToOneField('Menu', on_delete=models.CASCADE, related_name='branches')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='branches')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='branches')
    details = models.TextField()
    date_of_register = models.DateField(auto_now_add=True)

    @property
    def date_of_register_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.date_of_register)

    def __str__(self) -> str:
        return f"{self.restaurant}'\n'branch: {self.address} {self.date_of_register_jalali}"


class Food(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    category = models.ManyToManyField(Category, related_name='foods')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
    date_of_record = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='foods/')

    @property
    def date_of_record_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.date_of_record)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='menuItems')
    price = models.FloatField()
    number_of_existance = models.PositiveIntegerField()


    def __str__(self) -> str:
        return f"food: {self.food.name}'\n'price: {self.price}'\n'number: {self.number_of_existance}"


class Menu(models.Model):
    item = models.ManyToManyField(MenuItem, related_name='menus')


    def __str__(self):
        return " , ".join(item.food.name for item in self.item.all())


class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='order_items')
    number = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.item.food.name


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
    menu = models.ManyToManyField(OrderItem, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)
    customers_status = models.CharField(max_length=1, choices=CUSTOMERS_STATUS, default='a')
    restaurant_status = models.CharField(max_length=1, choices=RESTAURANT_STATUS, default='r')
    total_price = models.FloatField(null=True)

    @property
    def order_time_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.order_time)

    def __str__(self):
        return f"{self.customer} {self.get_customers_status_display()}"


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    foods = models.ManyToManyField(Order, related_name='invoices')
    last_purchase = models.DateTimeField(auto_now=True)

    @property
    def last_purchase_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.last_purchase)

    def __str__(self):
        return self.customer.user.username
