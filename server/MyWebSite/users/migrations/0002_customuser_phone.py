# Generated by Django 2.2.17 on 2021-08-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Телефон для связи'),
        ),
    ]
