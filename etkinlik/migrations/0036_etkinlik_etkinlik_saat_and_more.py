# Generated by Django 4.2.4 on 2023-08-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0035_etkinlik_etkinlik_banner_resim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='etkinlik_saat',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='etkinlik_tarihi',
            field=models.DateField(null=True),
        ),
    ]
