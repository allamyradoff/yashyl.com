# Generated by Django 4.1.7 on 2023-03-20 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_storeproduct_slug_storeproduct_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeproduct',
            name='stock',
        ),
    ]
