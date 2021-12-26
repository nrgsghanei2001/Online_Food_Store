from django.db import models


class Category(models.Model):
    MEAL_CHOICES = (('bf', 'Break Fast'),
    ('ld', 'Lunch And Dinner'),
    ('sn', 'Snack'))

    name = models.CharField(max_length=50)
    meal = models.CharField(max_length=2, choices=MEAL_CHOICES, default='ld')


    def __str__(self):
        return f"{self.name} {self.get_meal_display()}"
