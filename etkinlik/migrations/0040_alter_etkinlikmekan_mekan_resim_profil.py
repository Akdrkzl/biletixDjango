# Generated by Django 4.2.4 on 2023-08-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0039_etkinlik_stok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etkinlikmekan',
            name='mekan_resim_profil',
            field=models.FileField(blank=True, upload_to='etkinlik/', verbose_name='Mekan Profil Resmi'),
        ),
    ]
