# Generated by Django 4.2.4 on 2023-09-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0068_alter_sepet_miktar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='fiyat',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sepet',
            name='miktar',
            field=models.PositiveIntegerField(),
        ),
    ]
