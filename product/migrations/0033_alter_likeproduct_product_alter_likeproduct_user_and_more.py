# Generated by Django 4.0.6 on 2023-02-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_alter_likeproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeproduct',
            name='product',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='likeproduct',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='likeproduct',
            unique_together={('user', 'product')},
        ),
    ]
