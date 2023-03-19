from django.urls import path
from . import views


urlpatterns = [
	path('store-list/', views.storeList, name="store-list_mobile"),
	path('store-detail/<int:id>/', views.storeDetailList, name="store-detail_mobile"),
]