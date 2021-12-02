# Generated by Django 2.0.7 on 2021-12-02 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoKomponen',
            fields=[
                ('id_info_komponen', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='JenisInfo',
            fields=[
                ('id_jenis_info', models.AutoField(primary_key=True, serialize=False)),
                ('jenis_info', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='JenisKomponen',
            fields=[
                ('id_jenis_komponen', models.AutoField(primary_key=True, serialize=False)),
                ('jenis_komponen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Komponen',
            fields=[
                ('id_komponen', models.AutoField(primary_key=True, serialize=False)),
                ('nama_komponen', models.CharField(max_length=150)),
                ('harga_komponen', models.DecimalField(decimal_places=2, max_digits=11)),
                ('gambar_komponen', models.ImageField(upload_to='images/')),
                ('jenis_komponen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arctic_geeks_app.JenisKomponen')),
            ],
        ),
        migrations.AddField(
            model_name='infokomponen',
            name='jenis_info',
            field=models.ForeignKey(db_column='id_jenis_komponen', on_delete=django.db.models.deletion.CASCADE, to='arctic_geeks_app.JenisKomponen'),
        ),
        migrations.AddField(
            model_name='infokomponen',
            name='nama_komponen',
            field=models.ForeignKey(db_column='id_komponen', on_delete=django.db.models.deletion.CASCADE, to='arctic_geeks_app.Komponen'),
        ),
    ]
