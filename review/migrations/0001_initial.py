# Generated by Django 4.2.4 on 2023-08-18 10:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('path', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 일시')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('writer', models.CharField(blank=True, default='익명', max_length=30)),
                ('rating', models.PositiveIntegerField(blank=True, default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(null=True)),
                ('path_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='path.path')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
