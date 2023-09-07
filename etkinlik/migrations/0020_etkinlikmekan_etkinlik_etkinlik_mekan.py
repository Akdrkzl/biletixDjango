# Generated by Django 4.2.4 on 2023-08-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0019_rename_parent_etkinlik_kategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtkinlikMekan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mekan_resim_profil', models.FileField(upload_to='etkinlik/', verbose_name='Profil Resmi')),
                ('oturma_plani_resim', models.FileField(upload_to='etkinlik/', verbose_name='Profil Resmi')),
                ('mekan_resim', models.FileField(upload_to='etkinlik/', verbose_name='Profil Resmi')),
                ('isim', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=50)),
                ('aciklama', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='etkinlik_mekan',
            field=models.ManyToManyField(to='etkinlik.etkinlikmekan'),
        ),
    ]