# Generated by Django 4.0.6 on 2023-01-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_remove_product_pr'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cource_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
