# Generated by Django 4.2.4 on 2023-08-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0044_sepet'),
    ]

    operations = [
        migrations.AddField(
            model_name='sepet',
            name='resim',
            field=models.FileField(blank=True, upload_to='sepet/', verbose_name='Profil Resmi'),
        ),
    ]
