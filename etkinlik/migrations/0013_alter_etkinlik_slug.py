# Generated by Django 4.2.4 on 2023-08-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0012_etkinlik_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etkinlik',
            name='slug',
            field=models.SlugField(blank=True, default=0, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
