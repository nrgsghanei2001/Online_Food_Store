from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class FoodSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Food
        fields = '__all__'