from os import name
from django.urls import path
from . import views


urlpatterns = [
	path('ad-list/', views.AdListView.as_view(), name="ad-list_mobile"),
	path('ad-add/', views.AdCreateView.as_view(), name="ad-add_mobile"),
	path('edit-add/<int:pk>/', views.AdCreateView.as_view(), name="edit-add_mobile"),
	path('delete-add/<int:pk>/', views.AdsDelete.as_view(), name="delete-add_mobile"),
	path('ad-detail/<int:pk>/', views.AdsDetail.as_view(), name="ad-detail_mobile"),
	path('last-ads/', views.LastAds.as_view(), name="last-ads_mobile"),
]