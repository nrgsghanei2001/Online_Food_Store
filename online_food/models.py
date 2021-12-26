from django.db import models
from accounts.models import Address


class Category(models.Model):
    MEAL_CHOICES = (('bf', 'Break Fast'),
    ('ld', 'Lunch And Dinner'),
    ('sn', 'Snack'))

    name = models.CharField(max_length=50)
    meal = models.CharField(max_length=2, choices=MEAL_CHOICES, default='ld')


    def __str__(self):
        return f"{self.name} {self.get_meal_display()}"


class Restaurant(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='branches')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="branch")
    # foods = models.ManyToManyField('Food', related_name='branches')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='branches')
    details = models.TextField()
    date_of_register = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.restaurant}'\n'branch: {self.address}"


# class Food(models.Model):
