# Generated by Django 4.2.4 on 2023-08-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0024_alter_etkinlikmekan_aciklama'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
