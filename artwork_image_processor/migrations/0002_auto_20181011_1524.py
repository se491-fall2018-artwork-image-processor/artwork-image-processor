# Generated by Django 2.1.2 on 2018-10-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork_image_processor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='tmp/'),
        ),
    ]
