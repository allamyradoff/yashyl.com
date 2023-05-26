from django.db import models
from accounts.models import Account
from PIL import Image

class CategoryAd(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ady")
    image = models.ImageField(upload_to='category_ads/', blank=True, null=True, verbose_name="Surat")


    def ad_count(self):
        ac = Ad.objects.filter(cat_id=self.id)
        count = ac.count()
        return count

    def __str__(self):
        return self.name

class Locations(models.Model):
    title = models.CharField(max_length=255, verbose_name="Beýany")
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name="children", on_delete=models.PROTECT, verbose_name="Esasy")
    description = models.TextField(blank=True, null=True, verbose_name="Beýany")
    image = models.ImageField(upload_to="locations/", null=True, blank=True, verbose_name="Suraty")


    def loc_count(self):
        pc = Ad.objects.filter(locations=self.id)
        count = pc.count()
        return count

    def __str__(self):
        return self.title


class Ad(models.Model):
    # LOC_CATEGORY = [
    #     ('Mary', 'Mary'),
    #     ('Ashgabat', 'Ashgabat'),
    #     ('Lebap', 'Lebap'),
    #     ('Ahal', 'Ahal'),
    #     ('Balkan', 'Balkan'),
    #     ('Dashoguz', 'Dashoguz'),
    # ]
    name = models.CharField(max_length=255, verbose_name="Ady")
    desc = models.TextField(blank=True, null=True, verbose_name="Beýany")
    image = models.ImageField(upload_to='ad_test/', blank=True, null=True, verbose_name="Surat")
    image_2 = models.ImageField(upload_to='ad_test/', blank=True, null=True, verbose_name="Surat")
    image_3 = models.ImageField(upload_to='ad_test/', blank=True, null=True, verbose_name="Surat")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon belgi")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    seen_count = models.IntegerField(blank=True, null=True, default=0, verbose_name="Görülenler")
    locations = models.CharField(max_length=255, verbose_name="Ýerleşýän ýeri")

    
    
    # cat_id = models.ForeignKey(CategoryAd, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kategoriýa")
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, verbose_name="Müşderi")

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return f'{self.user.first_name} - {self.name}'

    def save(self, *args, **kwargs):
        return super(Ad, self).save(*args, **kwargs) #



