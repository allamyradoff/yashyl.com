# Generated by Django 4.0.6 on 2023-01-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_remove_category_icon_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
