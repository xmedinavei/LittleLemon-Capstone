from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Booking, MenuItem


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MenuItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'