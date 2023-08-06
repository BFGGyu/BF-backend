# Generated by Django 4.2.4 on 2023-08-06 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('MUSEUM', '박물관'), ('ART GALLERY', '미술관'), ('EXHIBITION', '전시회')], max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('opening_time', models.TimeField(default='09:00:00')),
                ('closing_time', models.TimeField(default='18:00:00')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('line', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('fac_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.facility')),
                ('stat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.station')),
            ],
        ),
    ]
