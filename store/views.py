from django.shortcuts import render, redirect
from .models import *
from product.models import *
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from accounts.models import *
from django.contrib import messages, auth

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
    return render(request, 'store/main-admin.html')


def create_product(request):

    store = Store.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            user = request.user.id
            store = store.get(user_id=user)
            print(store)
            # form.store = store.id
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()


    context = {
        'form': form
    }
    return render(request, 'store/create_product.html', context)
