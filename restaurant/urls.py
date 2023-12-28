#define URL route for index() view
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, msg, MenuItemsView, SingleMenuItemView, BookingViewSet

router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('msg/', msg),
    path('api-token-auth/', obtain_auth_token),
]