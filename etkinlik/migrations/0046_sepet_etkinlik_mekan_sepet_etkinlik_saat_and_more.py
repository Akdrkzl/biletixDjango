# Generated by Django 4.2.4 on 2023-08-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0045_sepet_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='sepet',
            name='etkinlik_mekan',
            field=models.ManyToManyField(to='etkinlik.etkinlikmekan'),
        ),
        migrations.AddField(
            model_name='sepet',
            name='etkinlik_saat',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='sepet',
            name='etkinlik_tarihi',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sepet',
            name='isim',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
