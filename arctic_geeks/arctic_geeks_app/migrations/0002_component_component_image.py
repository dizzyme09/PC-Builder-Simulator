# Generated by Django 2.0.7 on 2021-12-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arctic_geeks_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='component_image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]