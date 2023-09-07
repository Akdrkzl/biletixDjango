from django.urls import path
from django.urls import reverse
from .views import *

urlpatterns = [
    path('etkinlik-kategori-detay/<slug:slug>', kategoriDetay , name='etkinlik-kategori-detay'),
    path('etkinlik-liste/<slug:slug>', etkinlikListe , name='etkinlik-liste'),
    path('etkinlik-detay/<slug:slug>', etkinlikDetay, name='etkinlik-detay'),
    path('etkinlik-bilet/<slug:slug>', etkinlikBiletDetay, name='etkinlik-bilet'),
    # sepet
    path('sepet/', sepet, name='sepet'),
    path('sepet-sil/<int:etkinlik_id>', sepetSil, name='sepet-sil'),
    path('sepet-hepsini-sil/', sepetHepsiniSil, name='sepet-hepsini-sil'),

    path('etkinlik-mekan/<slug:slug>', mekan, name='mekan'),
    path('search/', search, name='search'),
    path('search-bos/', searchBos, name='search-bos'),
]