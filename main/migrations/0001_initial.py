# Generated by Django 4.1.7 on 2023-12-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('owner', models.CharField(max_length=20)),
                ('dateIn', models.DateField()),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]