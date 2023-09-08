from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Kategori(MPTTModel):
    isim = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    altkategori_resim = models.FileField(blank=True, upload_to='kategori/', verbose_name='Kategori Resmi')
    slug = models.SlugField(null=True, blank=True,  db_index=True, editable=False)

    class MPTTMeta:
        level_attr = 'mptt-level'
        order_insertion_by = ['isim']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):                           
        full_path = [self.isim]                  
        k = self.parent
        while k is not None:
            full_path.append(k.isim)
            k = k.parent
        return ' > '.join(full_path[::-1])

class EtkinlikMekan(models.Model):
    sehir = models.CharField(max_length=50)
    isim = models.CharField(max_length=50)
    adres = models.TextField(max_length=500)
    aciklama = models.TextField(max_length=550)
    mekan_resim_profil = models.FileField(blank=True, upload_to='etkinlik/', verbose_name='Mekan Profil Resmi')
    oturma_plani_resim = models.FileField(blank=True, upload_to='etkinlik/', verbose_name='Oturma Planı')
    mekan_resim = models.FileField(blank=True, upload_to='etkinlik/', verbose_name='Mekan Resmi')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim

class Etkinlik(models.Model):
    isim = models.CharField(max_length=50)
    kategori = models.ForeignKey(Kategori, blank=True, null=True, on_delete=models.CASCADE)
    fiyat = models.PositiveIntegerField()
    aciklama = RichTextField()
    etkinlik_resim_profil = models.FileField(blank=True, upload_to='etkinlik/', verbose_name='Profil Resmi')
    etkinlik_carousel_resim = models.FileField(blank=True, upload_to='etkinlik/carousel', verbose_name='Carousel Resmi')
    etkinlik_banner_resim = models.FileField(blank=True, upload_to='etkinlik/banner', verbose_name='Banner Resmi')
    etkinlik_tarihi = models.DateField(null=True)
    etkinlik_saat = models.TimeField(null=True)
    etkinlik_mekan = models.ManyToManyField(EtkinlikMekan)
    stok = models.BooleanField(default=False)
    hot_ticket = models.BooleanField(default=False)
    one_cikan_index = models.BooleanField(default=False)
    carousel_index = models.BooleanField(default=False)
    tum_tr = models.BooleanField(default=False)
    muzik_index = models.BooleanField(default=False)
    sahne_index = models.BooleanField(default=False)
    spor_index = models.BooleanField(default=False)
    aile_index = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim
    
    @property
    def muzik_index_visible(self):
        return self.kategori is not None and self.kategori.parent == "Müzik"

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name

class Sepet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    isim = models.CharField(max_length=50)
    miktar = models.PositiveIntegerField()
    # fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    fiyat = models.PositiveIntegerField()
    etkinlik_tarihi = models.DateField(null=True)
    etkinlik_saat = models.TimeField(null=True)
    etkinlik_mekan = models.ManyToManyField(EtkinlikMekan)
    resim = models.FileField(blank=True, upload_to='sepet/', verbose_name='Profil Resmi')
    slug = models.SlugField(null=False, blank=True, unique=False, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim

class Adres(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ulke = models.CharField(max_length=100)
    sehir = models.CharField(max_length=100)
    ilce = models.CharField(max_length=100)
    acik_adres = models.CharField(max_length=255)
    adres_baslik = models.CharField(max_length=100)

    def __str__(self):
        return self.ulke

class Musteri(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    isim = models.CharField(max_length=100)
    soyisim = models.CharField(max_length=100)
    dogum_tarihi = models.DateField()
    email = models.EmailField()
    cep_telefonu = models.CharField(max_length=25)
   

    ERKEK = 'Erkek'
    KADIN = 'Kadın'

    CINSIYET_CHOICES = (
        (ERKEK, 'Erkek'),
        (KADIN, 'Kadın'),
    )
    cinsiyet = models.CharField(max_length=10, choices=CINSIYET_CHOICES, default=ERKEK)

    def __str__(self):
        return self.isim

