#define URL route for index() view
from django.urls import path, include
from rest_framework import routers
from .views import index, MenuItemsView, SingleMenuItemView, BookingViewSet

router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]