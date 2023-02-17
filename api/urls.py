from django.urls import path, include

urlpatterns = [
	path('user/', include('api.authorization.urls')),
	path('ad/', include('api.ad.urls')),
	path('product/', include('api.product.urls')),
	path('order/', include('api.orders.urls')),
	path('banner/', include('api.banner.urls')),

]