# Generated by Django 4.2.4 on 2023-09-06 11:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0069_alter_sepet_fiyat_alter_sepet_miktar'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='aciklama',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
