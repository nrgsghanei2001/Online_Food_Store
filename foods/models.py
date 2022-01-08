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
