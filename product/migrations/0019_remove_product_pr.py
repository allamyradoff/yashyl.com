# Generated by Django 4.0.6 on 2023-01-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_pr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pr',
        ),
    ]
