# Generated by Django 4.0.6 on 2023-01-16 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand'),
        ),
    ]
