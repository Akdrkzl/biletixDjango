# Generated by Django 4.2.4 on 2023-09-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0071_etkinlik_hot_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulke', models.CharField(max_length=100)),
                ('sehir', models.CharField(max_length=100)),
                ('ilce', models.CharField(max_length=100)),
                ('acik_adres', models.CharField(max_length=255)),
                ('adres_baslık', models.CharField(max_length=100)),
            ],
        ),
    ]