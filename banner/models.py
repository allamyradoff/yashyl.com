from pyexpat import model
from django.db import models
from product.models import *


class Slider(models.Model):
    slider_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Web slider")
    slider_mini_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Slider gysgaça beýan")
    slider_image = models.ImageField(
        upload_to="slider_banner/", blank=True, null=True, verbose_name="Slider suraty")
    slider_mobile = models.ImageField(
        upload_to="mobile_slider_banner/", blank=True, null=True, verbose_name="Mobile surat")

    def __str__(self):
        return self.slider_title


class MiniSlider(models.Model):
    lilte_banner_1 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True, verbose_name="Kiçi banner")
    lilte_banner_2 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True, verbose_name="Kiçi banner 2")
    slider_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kiçi banneryň beýany")
    slider_mini_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kiçi banneriň gysgaça beýany")
    big_banner_2 = models.ImageField(
        upload_to="big_banner/", blank=True, null=True, verbose_name="Uly banner")

    slider_mobile = models.ImageField(
        upload_to="mobile_slider_banner/", blank=True, null=True, verbose_name="Mobile banner")

    def __str__(self):
        return self.slider_title


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Haryt")
    mini_desc_1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Beýan")
    mini_desc_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Beýan")
    mini_desc_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Beýan")

    def __str__(self):
        return f'{self.product.name}'


class TopMiniProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Haryt")

    def __str__(self):
        return f'{self.product.name}'


class BannerForCharity(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ady")
    desc = models.TextField(blank=True, null=True, verbose_name="Beýany")
    image = models.ImageField(upload_to='Charity/', blank=True, null=True, verbose_name="Suraty")

    image_mobile = models.ImageField(
        upload_to="mobile_charity_banner/", blank=True, null=True, verbose_name="Mobile suraty")


class StoreBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Beýan")
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True, verbose_name="Surat")


    

    def __str__(self):
        return self.title


class Cartbanner(models.Model):
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True, verbose_name="Surat")


class Logo(models.Model):
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True, verbose_name="Logo")
    image_mobile = models.ImageField(
        upload_to="store_banner/", blank=True, null=True, verbose_name="Mobile logo")


class CheckoutBanner(models.Model):
    image = models.ImageField(
        upload_to="checkout_banner/", blank=True, null=True, verbose_name="Surat")
