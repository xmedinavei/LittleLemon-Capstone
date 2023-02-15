from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .models import Menu, Booking
from .serializers import MenuModelSerializer, BookingModelSerializer, UserModelSerializer


# User
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserModelSerializer
   # permission_classes = [permissions.IsAuthenticated]

# Booking
class BookingViewSet (viewsets.ModelViewSet):
    serializer_class = BookingModelSerializer
    queryset = Booking.objects.all()


# Menu
class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer


class SingleMenuItemView (RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer
