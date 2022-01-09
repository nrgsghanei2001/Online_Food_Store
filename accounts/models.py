from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(max_length=50)
    address = models.TextField()
    phone = PhoneNumberField(null=True, blank=True, unique=True)


    def __str__(self):
        return f"{self.city}, {self.address}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.ManyToManyField(Address, related_name='customers', blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return self.device
   
