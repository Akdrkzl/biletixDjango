# Generated by Django 4.2.4 on 2023-09-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0047_sepet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sepet',
            name='fiyat',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
