from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister , name='register'),
    path('login/', userLogin , name='login'),
    path('logout/', userLogout , name='logout'),
    # hesap-bilgileri
    path('hesabim/', hesabim , name='hesabim'),
    path('kisisel-bilgiler/', kisiselBilgilerDegistir , name='profil'),
    path('sifre-degistir/', sifreDegistir , name='sifre-degistir'),
    path('adres/', adresDegistir , name='adres'),
    path('bildirim/', bildirimTercihleri , name='bildirim'),
    path('gelecek-bilet/', gelecekBilet , name='gelecek-bilet'),
    path('gecmis-bilet/', gecmisBilet , name='gecmis-bilet'),
    path('sezonluk-bilet/', sezonlukBilet , name='sezonluk-bilet'),
]