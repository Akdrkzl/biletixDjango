# Generated by Django 4.2.4 on 2023-09-05 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0065_alter_musteri_adres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musteri',
            name='adres',
        ),
    ]
