# Generated by Django 4.0.4 on 2023-05-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
