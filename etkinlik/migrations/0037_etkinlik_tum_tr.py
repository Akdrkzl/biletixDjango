# Generated by Django 4.2.4 on 2023-08-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0036_etkinlik_etkinlik_saat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='tum_tr',
            field=models.BooleanField(default=False),
        ),
    ]