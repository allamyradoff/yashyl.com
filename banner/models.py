from pyexpat import model
from django.db import models
from product.models import *


class Slider(models.Model):
    slider_title = models.CharField(max_length=100, blank=True, null=True)
    slider_mini_title = models.CharField(max_length=100, blank=True, null=True)
    slider_image = models.ImageField(
        upload_to="slider_banner/", blank=True, null=True)
    slider_mobile = models.ImageField(
        upload_to="mobile_slider_banner/", blank=True, null=True)

    def __str__(self):
        return self.slider_title


class MiniSlider(models.Model):
    lilte_banner_1 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)
    lilte_banner_2 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)
    slider_title = models.CharField(max_length=100, blank=True, null=True)
    slider_mini_title = models.CharField(max_length=100, blank=True, null=True)
    big_banner_2 = models.ImageField(
        upload_to="big_banner/", blank=True, null=True)

    slider_mobile = models.ImageField(
        upload_to="mobile_slider_banner/", blank=True, null=True)

    def __str__(self):
        return self.slider_title


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    link = models.CharField(max_length=255, blank=True, null=True)
    mini_desc_1 = models.CharField(max_length=50, blank=True, null=True)
    mini_desc_2 = models.CharField(max_length=50, blank=True, null=True)
    mini_desc_3 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.product.name}'


class TopMiniProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'


class BannerForCharity(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Charity/', blank=True, null=True)

    image_mobile = models.ImageField(
        upload_to="mobile_charity_banner/", blank=True, null=True)


class StoreBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)


    

    def __str__(self):
        return self.title


class Cartbanner(models.Model):
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)


class Logo(models.Model):
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)
    image_mobile = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)


class CheckoutBanner(models.Model):
    image = models.ImageField(
        upload_to="checkout_banner/", blank=True, null=True)
