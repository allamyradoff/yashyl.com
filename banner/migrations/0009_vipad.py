# Generated by Django 4.0.6 on 2022-10-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0008_alter_topproduct_mini_desc_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VipAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(blank=True, max_length=50, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='litle_banner/')),
                ('title_2', models.CharField(blank=True, max_length=50, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='litle_banner/')),
                ('title_3', models.CharField(blank=True, max_length=50, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='litle_banner/')),
            ],
        ),
    ]
