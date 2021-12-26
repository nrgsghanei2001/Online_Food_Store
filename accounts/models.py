from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    city = models.CharField(max_length=50)
    address = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)


    def __str__(self):
        return f"{self.city}, {self.address}'\n'phone number: {self.phone}"


