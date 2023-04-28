# Generated by Django 4.0.4 on 2023-04-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0020_remove_topproduct_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniAboutUsLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon_mini_about/', verbose_name='iconkasy')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Ady')),
                ('mini_desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MiniAboutUsRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Ady')),
                ('mini_desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
