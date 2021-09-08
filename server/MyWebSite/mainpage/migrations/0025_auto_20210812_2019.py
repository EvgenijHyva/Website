# Generated by Django 2.2.17 on 2021-08-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0024_auto_20210812_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='WhatsApp',
            new_name='whatsapp',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='telegram_username',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, unique=True, verbose_name='имя пользователя для Телеграм'),
        ),
    ]