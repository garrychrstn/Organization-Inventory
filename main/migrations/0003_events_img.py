# Generated by Django 4.1.7 on 2023-12-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='img',
            field=models.CharField(default='no img', max_length=100),
        ),
    ]
