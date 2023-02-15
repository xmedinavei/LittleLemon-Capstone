from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Booking, Menu


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'