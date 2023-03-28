from email import message
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib import messages, auth
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from news.models import *



news = News.objects.all()

def newsList(request):
    
    # print(news)

    context = {
        'news':news
    }
    return render(request, 'news/news-list.html', context)



def newsDetail(request, id):
    news = News.objects.get(id=id)

    # return HttpResponse(news.id)
    context = {
        'news':news,
    }
    return render(request, 'news/news-detail.html', context)