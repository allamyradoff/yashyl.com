from django.urls import path
from .views import *



urlpatterns = [
    path('', login_page, name="login-user"),
    path('admin-user/', base_user_admin, name="admin-user"),
    path('create-product', create_product, name="create-product"),
    path('update-product/<int:id>/', update_product, name="update_product"),
    path('delete-product/<int:id>/', delete_product, name="delete_product"),
	path('admin-logout/', logout, name="admin-logout"),


	path('stores/', stores, name="stores"),


]