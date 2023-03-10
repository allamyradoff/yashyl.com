from django.db import models
from product.models import Product, Variation
from accounts.models import Account

class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, verbose_name="Müşderi")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Haryt")
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, verbose_name="Sebet")
    quantity = models.IntegerField(verbose_name="Sany")
    is_active = models.BooleanField(default=True, verbose_name="Aktiwlygy")

    def sub_total(self):
        return self.product.price * self.quantity


    def __str__(self):
        return self.product.name