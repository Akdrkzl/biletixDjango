# Generated by Django 4.2.4 on 2023-08-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0030_remove_etkinlik_aile_index_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='muzik_index',
            field=models.BooleanField(default=False),
        ),
    ]
