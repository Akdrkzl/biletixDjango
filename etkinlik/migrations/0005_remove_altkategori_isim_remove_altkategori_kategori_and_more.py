# Generated by Django 4.2.4 on 2023-08-18 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0004_remove_kategori_ust_kategori_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='altkategori',
            name='isim',
        ),
        migrations.RemoveField(
            model_name='altkategori',
            name='kategori',
        ),
        migrations.RemoveField(
            model_name='altkategori',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='altkategori',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='isim',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='kategori',
        ),
        migrations.RemoveField(
            model_name='etkinlik',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='kategori',
            name='slug',
        ),
        migrations.AddField(
            model_name='altkategori',
            name='ad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='ad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='alt_kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alt_kategori_etkinlikleri', to='etkinlik.altkategori'),
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='ana_kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ana_kategori_etkinlikleri', to='etkinlik.kategori'),
        ),
        migrations.AlterField(
            model_name='altkategori',
            name='ust_kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alt_kategoriler', to='etkinlik.kategori'),
        ),
    ]
