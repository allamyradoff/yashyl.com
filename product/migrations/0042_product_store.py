# Generated by Django 4.1.7 on 2023-04-05 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_store_desc_store_logo'),
        ('product', '0041_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]
