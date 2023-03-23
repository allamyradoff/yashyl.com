from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from product.models import *
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from accounts.models import *
from django.contrib import messages, auth


"""Функции для админки клиентов """

def login_page(request):

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:

            auth.login(request, user)
            messages.success(request, 'Siz sistema girdiňiz')

            return redirect('admin-user')
        else:
            messages.error(request, 'Login ýa-da Parol nädogry')
            return redirect('login-user')

    return render(request, 'store/login.html')



def base_user_admin(request):
    user = request.user
    store = Store.objects.filter(user_id=user)
    store = store.last()
    # print(store.id)

    store_prod = StoreProduct.objects.filter(store=store)
    # print(store_prod)

    context = {
        'store_prod': store_prod,
    }

    return render(request, 'store/main-admin.html', context)


def create_product(request):
    user = request.user.id
    # print(user)
    store = Store.objects.all()
    store = store.get(user_id=user)




    try: 
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
                form.user = request.user                
                form.save()
                return redirect('admin-user')
        else:
            form = ProductForm()
    except:
        return HttpResponse('suraty girizmegiňizi haýyş edýäris')
    
    


    context = {
        'form': form,
        'store':store,
    }
    return render(request, 'store/create_product.html', context)


def update_product(request, id): 
    user = request.user.id
    # print(user)
    store = Store.objects.all()
    store = store.get(user_id=user)
   
    product = StoreProduct.objects.get(id=id)
    category = Category.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin-user')

    context = {
        'prod':product,
        'form':ProductForm(instance=product),
        'store':store,
    }


    return render(request, 'store/update_product.html', context)



def delete_product(request, id):
    shop = StoreProduct.objects.get(id=id)
    shop.delete()
    return redirect('admin-user')





def logout(request):
    auth.logout(request)
    messages.success(request, 'Siz sistemadan çykdyňyz')
    return redirect('store-list_mobile')






"""Функции для самого сайта"""


def stores(request):
    return render(request, 'store/web/shop.html')