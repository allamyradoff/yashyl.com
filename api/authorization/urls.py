from os import name
from django.urls import path
from . import views



urlpatterns = [
	path('login/', views.MyTokenObtainPairView.as_view(), name="login_mobile"),
	path('register/', views.registerUser, name="register_mobile"),
	path('create_profile/', views.AccountProfileView.as_view(), name="create_profile_mobile"),
	path("profile-delete/<int:pk>/", views.ProfileDelete.as_view(), name="profile-delete_mobile"),
]