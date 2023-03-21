from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class NewsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class News(models.Model):
    """Mobile"""
    banner_mobile = models.ImageField(upload_to='news_mobile_banner/', blank=True, null=True)
    title_mobile = models.CharField(max_length=255, blank=True, null=True)
    desc_mobile = models.TextField(blank=True, null=True)

    """Desctop"""
    banner = models.ImageField(upload_to='news_banner/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(
        blank=True, null=True, verbose_name="Giňişleýin beýany")


    def __str__(self):
        return self.title

