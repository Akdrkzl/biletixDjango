# Generated by Django 4.2.4 on 2023-08-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0028_rename_is_carousel_etkinlik_one_cikan_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='aile_index',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='muzik_index',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='sahne_index',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='spor_index',
            field=models.BooleanField(default=False),
        ),
    ]
