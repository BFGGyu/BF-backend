# Generated by Django 4.2.4 on 2023-08-07 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]