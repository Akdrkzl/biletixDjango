# Generated by Django 4.2.4 on 2023-08-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0017_etkinlik_etkinlik_tarihi'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='etkinlik_resim_profil',
            field=models.FileField(default=1, upload_to='etkinlik/', verbose_name='Profil Resmi'),
            preserve_default=False,
        ),
    ]