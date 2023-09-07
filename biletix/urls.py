"""
URL configuration for biletix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user.views import *
from etkinlik.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('user/', include('user.urls')),
    path('etkinlik/', include('etkinlik.urls')),

    # footer-sayfaları
    path('yardim/', yardim , name="yardim"),
    path('satis-kanallari/', satisKanal , name="satis-kanallari"),
    path('hediye-kart/', hediyeKart , name="hediye-kart"),
    path('etkinlik-katılım/', etkinlikKatılım , name="etkinlik-katılım"),
    path('hesabım/', account , name="account"),
    path('hesap-oluştur/', createAccount , name="createaccount"),
    path('biz-kimiz/', bizKimiz , name="biz-kimiz"),
    path('kurum-politikası/', kurumPolitikası , name="kurum-politikası"),
    path('görsel-materyal/', görselMateryal , name="görsel-materyal"),
    path('bize-ulas/', bizeUlas , name="bize-ulas"),
    path('reklam-ver/', reklamVer , name="reklam-ver"),
    path('kariyer/', kariyer , name="kariyer"),
    path('sözlesme-politika/', sözlesmePolitika, name="sözlesme-politika"),
    path('ttk-bildirim/', ttkBildirim, name="ttk-bildirim"),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
