# Generated by Django 2.2.17 on 2021-08-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_pagesettings_addition_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesettings',
            name='insert_addition_code',
            field=models.BooleanField(default=False),
        ),
    ]
