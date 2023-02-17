from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('order-list/', views.UserOrderView.as_view(), name="order-list"),
    path('user-order-list/', views.UserOrderList.as_view(), name='user-order-list'),
    path('user-order-create/', views.OrderCreateView.as_view(), name="user-order-create"),
    path('order-details/<int:id>/', views.OrderItemsDetailView.as_view(), name='order-details'),
]