# Generated by Django 3.2.9 on 2021-12-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0016_alter_build_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='shortcode',
            field=models.CharField(blank=True, default=None, max_length=6, null=True, unique=True),
        ),
    ]