# Generated by Django 4.2.4 on 2023-08-20 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0029_etkinlik_aile_index_etkinlik_muzik_index_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etkinlik',
            name='aile_index',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='muzik_index',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='sahne_index',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='spor_index',
        ),
    ]
