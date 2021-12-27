from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    city = models.CharField(max_length=50)
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)


    def __str__(self):
        return f"{self.city}, {self.address}'\n'phone number: {self.phone}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers')
    email = models.EmailField(blank=True)
    address = models.ManyToManyField(Address, related_name='customers')


    def __str__(self):
        return self.user.username
   

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staffs')
    email = models.EmailField(blank=True)
    address = models.ManyToManyField(Address, related_name='staffs')


    def __str__(self):
        return self.user.username
