# Generated by Django 4.2.4 on 2023-08-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0011_etkinlik_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
