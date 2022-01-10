from django.db import models
from django.contrib.auth.models import User
from accounts.models import Address
from online_food.models import *


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staffs')
    email = models.EmailField(blank=True)
    # address = models.ManyToManyField(Address, related_name='staffs')
    restaurant = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='staffs', null=True, blank=True)

    def __str__(self):
        return self.user.username
