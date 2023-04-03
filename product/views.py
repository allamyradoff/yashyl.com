from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct
from banner.models import *
from django.db.models import Count
from accounts.models import UserProfile
from orders.models import OrderProduct
from carts.models import CartItem, Cart
from carts.views import _cart_id
from obyawleniya.models import CategoryAd
from django.db.models import Max, Min


def home(request):
    product = Product.objects.filter(is_active=True)
    category = Category.objects.all()

    product_sale = Product.objects.filter(is_active=True, is_sale=True)
    product_new = Product.objects.filter(is_active=True, is_new=True)

    top_product = TopProduct.objects.all()
    top_product = top_product[0]
    top_mini_product_all = TopMiniProduct.objects.all()
    top_mini_product = top_mini_product_all[0:2]
    top_mini_product_2 = top_mini_product_all[2:4]
    last_product = Product.objects.all()
    last_product = last_product.order_by('-id')
    last_product = last_product[0:6]

    banner_of_charity = BannerForCharity.objects.all()[:1]
    brands = Brand.objects.all()

    slider = Slider.objects.all()
    mini_slider = MiniSlider.objects.all()
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    """ Вариации категорий каторые требуется для шапки """

    category_1 = Category.objects.filter(name="Egin-eshik")
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
        'category': category,
        'slider': slider,
        'mini_slider': mini_slider,
        'product_sale': product_sale,
        'product_new': product_new,
        'top_product': top_product,
        'top_mini_product': top_mini_product,
        'top_mini_product_2': top_mini_product_2,
        'last_product': last_product,
        'logo': logo,
        'cart_items': cart_items,
        'ads_cat': ads_cat,
        'banner_of_charity': banner_of_charity,
        'brands': brands,
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
    return render(request, 'home.html', context)


def all_product(request):

    all_products = Product.objects.order_by('-id')
    category_count = all_products.count()
    category = Category.objects.all()[5:]
    store_banner = StoreBanner.objects.all()
    logo = Logo.objects.all()
    cource = Cours.objects.last()
    cource = cource.cours

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    paginator = Paginator(all_products, 8)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    ads_cat = CategoryAd.objects.all()

    """ Вариации категорий каторые требуется для шапки """

    category_1 = Category.objects.filter(name="Egin-eshik")
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
        'product': paged_products,
        'category': category,
        'category_count': category_count,
        'store_banner': store_banner,
        'logo': logo,
        'cart_items': cart_items,
        'ads_cat': ads_cat,
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

    return render(request, 'store.html', context)


def store(request, id):
    category = Category.objects.all()
    product = Product.objects.filter(category=id, is_active=True)
    product = product.order_by('-id')
    all_products = Product.objects.all()
    category_count = all_products.count()
    store_banner = StoreBanner.objects.all()
    logo = Logo.objects.all()

    paginator = Paginator(product, 8)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    current_id = id

    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    """ Вариации категорий каторые требуется для шапки """

    category_1 = Category.objects.filter(name="Egin-eshik")
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
        'product': paged_products,
        'category': category,
        'category_count': category_count,
        'store_banner': store_banner,
        'logo': logo,
        'cart_items': cart_items,
        'ads_cat': ads_cat,
        'current_id': current_id,

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
    return render(request, 'store.html', context)

def storeCategory(request, slug):

    cat = Category.objects.filter(name=slug)[:1]
    product = Product.objects.filter(category=cat).order_by("-id")


    all_products = Product.objects.all()
    category_count = all_products.count()
    store_banner = StoreBanner.objects.all()
    logo = Logo.objects.all()

    paginator = Paginator(product, 8)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    current_id = id

    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    """ Вариации категорий каторые требуется для шапки """

    category_1 = Category.objects.filter(name="Egin-eshik")
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
        'product': paged_products,
        'category': cat,
        'category_count': category_count,
        'store_banner': store_banner,
        'logo': logo,
        'cart_items': cart_items,
        'ads_cat': ads_cat,
        'current_id': current_id,

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


    return render(request, 'store.html', context)


def store_brands(request, id):
    category = Category.objects.all()
    product = Product.objects.filter(brands__id=id, is_active=True)
    product = product.order_by('-id')
    all_products = Product.objects.all()
    category_count = all_products.count()
    store_banner = StoreBanner.objects.all()
    logo = Logo.objects.all()

    paginator = Paginator(product, 8)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    current_id = id

    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    context = {
        'product': paged_products,
        'category': category,
        'category_count': category_count,
        'store_banner': store_banner,
        'logo': logo,
        'cart_items': cart_items,
        'ads_cat': ads_cat,

        'current_id': current_id

    }
    return render(request, 'store.html', context)


def product_detail(request, category_id, id):
    product = Product.objects.get(id=id)
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

    return render(request, 'product_detail.html', context)


def search(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    category_count = all_products.count()
    store_banner = StoreBanner.objects.all()
    ads_cat = CategoryAd.objects.all()
    logo = Logo.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.filter(name__icontains=keyword)
            product_count = product.count()

    context = {
        'product': product,
        'product_count': product_count,
        # 'category': category,
        'category_count': category_count,
        # 'store_banner': store_banner,
        'cart_items': cart_items,
        'ads_cat': ads_cat,
        'logo': logo

    }
    return render(request, 'store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(
                request, "Syn edeniňiz üçin sag boluň, synyňyz täzelendi.")
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                # data.ip = request.META.get('REMOTE_ADDR')

                data.product_id = product_id
                data.user_id = request.user.id
                data.save()

                messages.success(request, 'Syn edeniňiz üçin sag boluň')
                return redirect(url)
