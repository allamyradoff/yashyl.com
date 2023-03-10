from django.db import models

from accounts.models import Account



class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name="Dükanyň ady")
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Ulanyjy")


    def __str__(self):
        return self.name


class StoreProduct(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    sale_percent = models.CharField(max_length=10, blank=True, null=True)
    sale_price = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    def __str__(self):
        return self.name





