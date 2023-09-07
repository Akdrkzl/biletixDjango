from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from etkinlik.models import *
# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        isim = request.POST['isim']
        soyisim = request.POST['soyisim']
        email = request.POST['email']
        sifre = request.POST['sifre']
        dogum_tarihi = request.POST['dogum-tarihi']
        cep_telefonu = request.POST['telefon']
        cinsiyet = request.POST['cinsiyet']


        if User.objects.filter(email = email).exists():
            messages.error(request,'Bu Mail Adresi Zaten Kullanılıyor.')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username =  email, email = email, first_name = isim, last_name = soyisim, password = sifre,
            )
            musteri = Musteri.objects.create(
                user = user, isim = isim, soyisim = soyisim,  email = email, dogum_tarihi = dogum_tarihi, cinsiyet = cinsiyet, cep_telefonu = cep_telefonu
            )
            musteri.save()
            user.save()
            messages.success(request, 'Kullanıcı Oluşturuldu')
            return redirect('login')

    else:
        return render(request,'hesapolustur.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Başarılı')
            return redirect('index')
         # Başarılı giriş durumunda index sayfasına yönlendir
        else:
            messages.error(request, 'Kullanıcı Adı veya Şifre Yanlış')
            return redirect('login')

    return render(request,'girisyap.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('login')

def hesabim(request):
    return render(request,'hesabim.html')

def kisiselBilgilerDegistir(request):
    if request.method == 'POST':
        yeniİsim = request.POST['isim']
        yeniSoyİsim = request.POST['soy-isim']
        dogum_tarihi = request.POST['dogum-tarihi']
        cinsiyet = request.POST['cinsiyet']

        user = request.user
        musteri = Musteri.objects.get(user = user)
        user.first_name = yeniİsim
        user.last_name = yeniSoyİsim
        musteri.isim = yeniİsim
        musteri.soyisim = yeniSoyİsim
        musteri.dogum_tarihi = dogum_tarihi
        musteri.cinsiyet = cinsiyet
        musteri.save()
        user.save()
        messages.success(request,'Kullanıcı Bilgileri Başarıyla Değiştirildi')
        return redirect('profil')
    return render(request,'hesabim-bilgileri.html')

def sifreDegistir(request):
    if request.method == 'POST':
        mevcutSifre = request.POST['mevcut-sifre']
        yeniSifre = request.POST['yeni-sifre']
        yeniSifreTekrar = request.POST['yeni-sifre-tekrar']

        user = request.user
        if user.check_password(mevcutSifre):
            if yeniSifre == yeniSifreTekrar:
                user.set_password(yeniSifre)
                user.save()
                update_session_auth_hash(request,user)
                messages.success(request,'Şifre Başarılı Bir Şekilde Değiştirildi')
                return redirect('sifre-degistir')
        else:
            messages.error(request, 'Mevcut Şifre Yanlış veya Yeni Şifreler Eşleşmiyor')
            return redirect('sifre-degistir')

    return render(request,'hesabim-sifre-degistir.html')

def adresDegistir(request):
    if request.method == 'POST':
        ulke = request.POST['ulke']
        sehir = request.POST['sehir']
        ilce = request.POST['ilce']
        acik_adres = requst.POST['acik-adres']
        adres_başlık = request['adres-baslik']

        user = request.user
        adres = Adres.objects.get(user = user)
        adres.ulke = ulke
        adres.sehir = sehir
        adres.ilce = ilce
        adres.acik_adres = acik_adres
        adres.adres_baslik = adres_baslik
        adres.save()
        return redirect('profil')
    return render(request,'hesabim-adres.html')

def bildirimTercihleri(request):
    return render(request,'hesabim-bildirim.html')

def gelecekBilet(request):
    return render(request,'hesabim-gelecek-bilet.html')

def gecmisBilet(request):
    return render(request,'hesabim-gecmis-bilet.html')

def sezonlukBilet(request):
    return render(request,'hesabim-sezonluk-bilet.html')