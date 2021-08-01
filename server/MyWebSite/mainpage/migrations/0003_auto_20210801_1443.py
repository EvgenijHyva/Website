# Generated by Django 2.2.17 on 2021-08-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20210731_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecontent',
            options={'verbose_name': 'контент на страницу главная', 'verbose_name_plural': 'Главная (контент страницы)'},
        ),
        migrations.RemoveField(
            model_name='pagecontent',
            name='content',
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='about',
            field=models.TextField(blank=True, verbose_name='about'),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='show_image',
            field=models.BooleanField(default=True),
        ),
    ]
