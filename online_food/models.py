from django.db import models
from django.db.models.base import Model
from accounts.models import Address


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
