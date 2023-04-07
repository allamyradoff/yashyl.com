from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from product.models import *
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from accounts.models import *
from django.contrib import messages, auth


from django.http import HttpResponse
from django.contrib import messages
from orders.models import OrderProduct
from banner.models import *
from accounts.models import UserProfile
from orders.models import OrderProduct
from carts.models import CartItem, Cart
from carts.views import _cart_id
from obyawleniya.models import CategoryAd




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
    store = Store.objects.all()
    context = {
        'store': store,
    }
    return render(request, 'store/web/stores.html', context)




def store_products(request, id):
    # product = Product.objects.all()
    product = Product.objects.filter(is_active=True, is_store=True, store=id)
    print(product)

    context = {
        'product':product,
    }
    return render(request, 'store/web/store_products.html', context)



def product_detail(request, category_id, id, store_id):
    product = Product.objects.get(id=id, is_store=True)
    cat_prod = Product.objects.all()
    cat_prod = cat_prod.filter(store=store_id).exclude(id=id)
    print(cat_prod)
    logo = Logo.objects.all()

    # if request.user.is_authenticated:

    #     try:
    #         orderproduct = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()
    #     except OrderProduct.DoesNotExist:
    #         orderproduct = None

    # else:
    #     orderproduct = None

    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    reviews_count = reviews.count()

    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    if request.user.is_authenticated:

        profile = UserProfile.objects.filter(user=request.user)
    else:
        profile = None

        """ Вариации категорий каторые требуется для шапки """

    category_1 = Category.objects.filter(name="Sport eşikleri")
    category_2 = Category.objects.filter(name="Oy bezegleri")
    category_3 = Category.objects.filter(name="Hojalyk harytlary")
    category_4 = Category.objects.filter(name="Kompyuter tehnikalary")
    category_5 = Category.objects.filter(name="Gozellik we ideg serishdeleri")
    category_6 = Category.objects.filter(name="Awtobezegler")
    category_7 = Category.objects.filter(name="Sport we guymenje")
    category_8 = Category.objects.filter(name="Telefon aksessuarlary")
    category_9 = Category.objects.filter(name="Konselyariya harytlary")
    category_10 = Category.objects.filter(name="Gap-gachlar")



    

    context = {
        'product': product,
        # 'orderproduct': orderproduct,
        'reviews': reviews,
        'profile': profile,
        'reviews_count': reviews_count,
        'logo': logo,
        'cart_items': cart_items,
        'ads_cat': ads_cat,
        'cat_prod':cat_prod,

        'category_1': category_1,
        'category_2': category_2,
        'category_3': category_3,
        'category_4': category_4,
        'category_5': category_5,
        'category_6':category_6,
        'category_7':category_7,
        'category_8':category_8,
        'category_9':category_9,
        'category_10':category_10,

    }

    return render(request, 'store/web/product_detail.html', context)
