# Generated by Django 4.1.7 on 2023-03-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
