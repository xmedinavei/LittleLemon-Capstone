from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MenuItemsView, SingleMenuItemView, BookingViewSet


router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='tables')

urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),

    path('booking/', include(router.urls)),
]

# urlpatterns += router.urls
