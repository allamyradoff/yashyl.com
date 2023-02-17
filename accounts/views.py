from email import message
from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


from carts.views import _cart_id
from carts.models import Cart, CartItem
from orders.models import Order, OrderProduct
from banner.models import Logo
from obyawleniya.models import CategoryAd

def register(request):
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()
            

            user = authenticate(phone_number=phone_number, password=password)
            if user is not None:          

                auth.login(request, user)
                messages.success(request, 'Siz sistema girdiňiz')

                return redirect('home')
            else:
                messages.error(request, 'Login ýa-da Parol nädogry')
                return redirect('login')

            # активация аккаунта
            
            # current_site = get_current_site(request)
            # mail_subject = 'Пожалыста активирвуйти ваш аккаунт'
            # message = render_to_string('accounts/account_verification_email.html', {
            #     'user':user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = email
            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # send_email.send()

            messages.success(request, 'Hasaba alyş üstünlikli boldy')
            return redirect('store')

    else:
        form = RegisterForm()

    context = {
        'form': form,
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat
    }
    return render(request, 'accounts/login.html', context)


def login(request):
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0



    if request.method == 'POST':
        email = request.POST['phone_number']
        password = request.POST['password']

        user = auth.authenticate(phone_number=email, password=password)

        if user is not None:

            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))

                is_cart_item_exists = CartItem.objects.filter(
                    cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    for item in cart_item:
                        item.user = user
                        item.save()
                        print(item)

            except:
                print('except')
                pass

            auth.login(request, user)
            messages.success(request, 'Siz sistema girdiňiz')

            return redirect('home')
        else:
            messages.error(request, 'Login ýa-da Parol nädogry')
            return redirect('login')


        if request.method == "POST":
            form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()

            # активация аккаунта

            # current_site = get_current_site(request)
            # mail_subject = 'Пожалыста активирвуйти ваш аккаунт'
            # message = render_to_string('accounts/account_verification_email.html', {
            #     'user':user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = email
            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # send_email.send()
            messages.success(request, 'Hasaba alyş üstünlikli boldy')
            return redirect('login')

    else:
        form = RegisterForm()


    context = {
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'form':form,
    }

    return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Siz sistemadan çykdyňyz')
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):

    # user = request.user

    # user_profile = UserProfile.objects.filter(user=user)

    # if user_profile == 0:
    #     return redirect('register_profile')

    # if request.user.userprofile is not None:
    #     return redirect('register_profile')


    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    user = request.user


    try:

        order = Order.objects.order_by(
            '-created_at').filter(user_id=request.user.id, is_ordered=True)
        orders_count = order.count()

        userprofile = UserProfile.objects.get(user_id=request.user.id)

    except ObjectDoesNotExist:
        return redirect('register_profile')

    context = {
        'orders_count': orders_count,
        'userprofile': userprofile,
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat

    }
    return render(request, 'accounts/dashboard.html', context)


def my_orders(request):
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0
    order = Order.objects.filter(
        user_id=request.user, is_ordered=True).order_by('-created_at')

    context = {
        'order': order,
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat
    }
    return render(request, 'accounts/my_orders.html', context)


def register_profile(request):
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    user = request.user.id
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            address_line_1 = form.cleaned_data['address_line_1']
            state = form.cleaned_data['state']
            profile_avatar = request.FILES['profile_avatar']

            form = UserProfile.objects.create(
                user=request.user,
                address_line_1=address_line_1,
                state=state,
                profile_avatar=profile_avatar
            )
            form.save()
            return redirect('dashboard')

        else:
            return HttpResponse('Profil suraty girizmegiňizi haýyş edýäris')

    context = {
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat
    }

    return render(request, 'accounts/register_profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0
    
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliňiz täzelendi')
            return redirect('edit_profile')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat

    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def changePassword(request):
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()

                messages.success(request, 'Parolyňyz üýtgedildi')
                return redirect('changePassword')

            else:
                messages.error(
                    request, 'Iki paroly dogry giriziň')
                return redirect('changePassword')
        else:
            messages.error(request, 'Parol gabat gelenok')
            return redirect('changePassword')


    context = {
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat

    }
    return render(request, 'accounts/changePassword.html', context)


# @login_required(login_url='login')
def order_detail(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    # order = Order.objects.get(order_number=order_id)
    context = {
        'order_detail': order_detail,
        # 'order': order
    }
    return render(request, 'accounts/order_detail.html', context)


