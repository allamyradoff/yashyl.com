# Generated by Django 4.0.4 on 2023-04-14 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0019_alter_bannerforcharity_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topproduct',
            name='link',
        ),
    ]
