# Generated by Django 4.2.4 on 2023-08-06 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_amenity_quantity_alter_facility_latitude_and_more'),
        ('path', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='longtitude',
        ),
        migrations.AddField(
            model_name='route',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='path',
            name='departure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.station'),
        ),
        migrations.AlterField(
            model_name='path',
            name='distance',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='path',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]
