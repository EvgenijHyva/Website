# Generated by Django 2.2.17 on 2021-08-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0022_auto_20210812_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='WhatsApp',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='Телефон для whatsapp'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='facebook',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='Сылка на facebook'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='github',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='Сылка на Гитхаб'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='instagram',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='Сылка на instagram'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='telegram',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='имя пользователя для телеграма'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='vk',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='Сылка на vk'),
        ),
    ]
