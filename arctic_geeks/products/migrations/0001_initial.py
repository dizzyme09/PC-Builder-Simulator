# Generated by Django 3.2.9 on 2021-12-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komponen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('manufaktur', models.CharField(blank=True, max_length=30)),
                ('nama_komponen', models.CharField(default='', max_length=120)),
                ('harga', models.PositiveIntegerField()),
                ('gambar', models.ImageField(blank=True, upload_to='images/')),
                ('link_tokopedia', models.URLField()),
                ('link_shopee', models.URLField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_products.komponen_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('form_factor', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('tipe', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('cores', models.PositiveIntegerField(default=2)),
                ('threads', models.PositiveIntegerField(default=4)),
                ('watts', models.PositiveIntegerField(default=0)),
                ('socket', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('kapasitas', models.CharField(max_length=10)),
                ('tipe', models.CharField(max_length=20)),
                ('form_factor', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('rpm_max', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('series', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('socket', models.CharField(max_length=15)),
                ('chipset', models.CharField(max_length=40)),
                ('form_factor', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('daya', models.PositiveIntegerField(default=0)),
                ('efisiensi', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('komponen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.komponen')),
                ('kapasitas', models.PositiveIntegerField(default=2)),
                ('tipe_channel', models.CharField(max_length=100)),
                ('kecepatan', models.PositiveIntegerField(default=2133)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.komponen',),
        ),
    ]