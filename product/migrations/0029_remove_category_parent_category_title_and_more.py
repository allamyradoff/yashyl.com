# Generated by Django 4.0.6 on 2023-01-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Sport eşikleri', 'Sport eşikleri'), ('Aýakgap', 'Aýakgap'), ('Meşhur harytlar', 'Meşhur harytlar'), ('Ýakynlaň üçin', 'Ýakynlaň üçin'), ('Özin üçin', 'Özin üçin')], default='Ayakgap', max_length=150),
        ),
    ]
