from django.urls import path
from .views import *


urlpatterns = [
    path('news-list/', newsList, name="news-list"),
    path('news-detail/<int:id>/', newsDetail, name="news-detail"),

]