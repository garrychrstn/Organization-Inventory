# Generated by Django 4.1.7 on 2023-12-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_events_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='uploaded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='reg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
