from django.urls import path
from .views import *



urlpatterns = [
    path('login-user', login_page, name="login-user"),
    path('admin-user', base_user_admin, name="admin-user"),
    path('create-product', create_product, name="create-product"),
]