from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# from online_food.models import Branch


class Address(models.Model):
    city = models.CharField(max_length=50)
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)


    def __str__(self):
        return f"{self.city}, {self.address}'\n'phone number: {self.phone}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.ManyToManyField(Address, related_name='customers', blank=True, null=True)
    device = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return self.device
   

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staffs')
    email = models.EmailField(blank=True)
    address = models.ManyToManyField(Address, related_name='staffs')
    # restaurant = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='staffs')

    def __str__(self):
        return self.user.username
