# Generated by Django 2.2.17 on 2021-08-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0018_auto_20210805_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='image',
            field=models.ImageField(blank=True, upload_to='MainPhoto', verbose_name='фото/картинка'),
        ),
    ]
