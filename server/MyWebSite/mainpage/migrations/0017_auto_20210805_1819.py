# Generated by Django 2.2.17 on 2021-08-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0016_pagesettings_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='image',
            field=models.ImageField(blank=True, height_field=500, upload_to='mainPhoto', verbose_name='фото/картинка', width_field=350),
        ),
    ]
