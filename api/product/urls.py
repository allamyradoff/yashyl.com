from os import name
from django.urls import path
from . import views


urlpatterns = [
	path('product-list/', views.ProductListView.as_view(), name="product-list_mobile"),
	path('category-list/', views.categoryList, name="category-list_mobile"),
	path('category/<int:pk>/', views.CategoryProductsView.as_view(), name="category-detail_mobile"),
	path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail_mobile"),
	path('product-get-like/', views.likeGetProduct, name="product-get-like_mobile"),
	path('product-like/', views.likeProduct, name="product-like_mobile"),
	path('product-like-delete/<int:pk>/', views.LikeProductDelete.as_view(), name="product-like-delete_mobile"),
]