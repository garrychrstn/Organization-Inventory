# Generated by Django 4.1.7 on 2023-12-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_goods_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='penerima',
            field=models.CharField(default='belum diisi', max_length=30),
        ),
    ]