# Generated by Django 4.2.4 on 2023-08-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0014_kategori_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
