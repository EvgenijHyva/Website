# Generated by Django 2.2.17 on 2021-08-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0019_auto_20210805_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='telegram',
            field=models.CharField(blank=True, max_length=256, unique=True, verbose_name='телефон для телеграма'),
        ),
    ]
