from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import MenuItemsView, SingleMenuItemView, BookingViewSet


router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='tables')

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),

    path('booking/', include(router.urls)),

    path('api-token-auth/', obtain_auth_token),
]

# urlpatterns += router.urls
