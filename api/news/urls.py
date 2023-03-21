from django.urls import path
from . import views


urlpatterns = [
	path('news-list/', views.newsList, name="news-list_mobile"),
	path('news-detail/<int:id>/', views.newsDetailList, name="news-detail_mobile"),
    
]