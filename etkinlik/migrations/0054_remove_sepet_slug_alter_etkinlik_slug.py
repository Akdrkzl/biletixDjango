# Generated by Django 4.2.4 on 2023-09-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0053_sepet_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sepet',
            name='slug',
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
