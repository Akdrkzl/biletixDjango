# Generated by Django 4.2.4 on 2023-09-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0058_rename_müsteri_musteri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteri',
            name='cinsiyet',
            field=models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], default='Erkek', max_length=10),
        ),
    ]
