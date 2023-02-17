from os import name
from django.urls import path
from . import views


urlpatterns = [
	path('slider-list/', views.sliderList, name="slider-list_mobile"),
	path('top-product-list/', views.topProductList, name="top-product-list_mobile"),
	path('top-mini-slider-list/', views.topMiniSliderList, name="top-mini-slider-list_mobile"),
	path('banner-for-charity/', views.bannerForCharityList, name="banner-for-charity_mobile"),

]