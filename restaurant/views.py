from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem, Booking
from .serializers import MenuItemModelSerializer, BookingModelSerializer, UserModelSerializer


# User
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserModelSerializer
   # permission_classes = [permissions.IsAuthenticated]

# Booking
class BookingViewSet (viewsets.ModelViewSet):
    serializer_class = BookingModelSerializer
    queryset = Booking.objects.all()


# MenuItem
class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer


class SingleMenuItemView (RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemModelSerializer
