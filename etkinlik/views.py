from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import *


# Create your views here.

def index(request):
    etkinlik = Etkinlik.objects.filter(
        Q(kategori__parent__isim = 'Müzik') |
        Q(kategori__parent__isim ='Sahne') |
        Q(one_cikan_index=True) |
        Q(tum_tr=True) |
        Q(muzik_index=True) |
        Q(sahne_index=True) |
        Q(spor_index=True) |
        Q(aile_index=True) 
    )


    etkinlik_tarih = Etkinlik.objects.all()
    context ={
        'etkinlik' : etkinlik,
        'etkinlik_tarih' : etkinlik_tarih,
    }
    return render(request, 'index.html', context)

def search (request):
    etkinlik = Etkinlik.objects.filter(
        Q(kategori__parent__isim = 'Müzik') |
        Q(kategori__parent__isim ='Sahne') |
        Q(one_cikan_index=True) |
        Q(tum_tr=True) |
        Q(muzik_index=True) |
        Q(sahne_index=True) |
        Q(spor_index=True) |
        Q(aile_index=True) 
        )
    
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        etkinlik = Etkinlik.objects.filter(
        Q(isim__icontains = search) |
        Q(etkinlik_mekan__isim__icontains = search) |
        Q(etkinlik_mekan__sehir__icontains = search) |
        Q(kategori__isim__icontains = search) 
    )
    if not etkinlik.exists():
        return redirect('search-bos')
    context={
        'etkinlik' : etkinlik,
        'search' : search,
    }
    return render (request, 'search.html',context)

def searchBos(request):
    
    return render (request, 'search-bos.html')


def kategoriDetay(request, slug):
    etkinlik = Etkinlik.objects.filter(kategori__parent__slug = slug)
    context ={
        'etkinlik' : etkinlik,
    }
    return render (request, 'kategoriDetay.html', context)

def etkinlikListe(request, slug):
    etkinlik = Etkinlik.objects.filter(
        Q(kategori__slug = slug)
        )
    mekan = EtkinlikMekan.objects.all()
    context ={
        'mekan' : mekan,
        'etkinlik' : etkinlik,
    }
    return render(request, 'etkinliklistedetay.html', context)

def etkinlikDetay(request,slug):
    etkinlik = Etkinlik.objects.filter(slug = slug)
    mekan = EtkinlikMekan.objects.all()
    user = request.user
    sepet = Sepet.objects.filter(user=user)
    
    # sepetteki-tüm-miktarı-görüntüler
    sepet_miktar = 0
    for sepet_item in sepet:
        sepet_miktar += sepet_item.miktar

    context ={
        'etkinlik' : etkinlik,
        'mekan' : mekan,
        'sepet_miktar' : sepet_miktar
    }

    return render (request, 'etkinlik_detay.html', context)

#Etkinlik-Bilet-Detay-Sayfası
def etkinlikBiletDetay(request,slug):
    etkinlik = Etkinlik.objects.filter(slug = slug)

    # model
    etkinlik_sepet = get_object_or_404(Etkinlik, slug = slug)
    mekan = EtkinlikMekan.objects.all()

    #kullancının sepetine erişiyor
    user = request.user
    sepet =  Sepet.objects.filter(user=user)
    # sepet = get_object_or_404(Sepet, user=user)


    # sepetteki-tüm-miktarı-görüntüler
    sepet_miktar = 0
    for sepet_item in sepet:
        sepet_miktar += sepet_item.miktar

    context ={
        'etkinlik' : etkinlik,
        'mekan' : mekan,
        'sepet_miktar': sepet_miktar,
    }
    
    # sayfadan miktar ve fiyat form ile alındı ve bir sepet oluşturuldu
    if request.method == 'POST':
        miktar = int(request.POST['miktar'])
        toplam_fiyat = float(request.POST['toplam-fiyat'])

        if request.user.is_authenticated:
            try:
                sepet_item = Sepet.objects.get(user=user, slug = slug)
                sepet_item.miktar += miktar
                sepet_item.fiyat += toplam_fiyat
                sepet_item.save()
                return redirect('sepet')
            # if Sepet.objects.filter(slug = slug).exists():
            #     sepet.miktar += miktar
            #     sepet.save()
            #     return redirect('index')
            except Sepet.DoesNotExist:
                sepet = Sepet.objects.create(
                    user = request.user,
                    miktar = miktar,
                    fiyat = toplam_fiyat,
                    isim = etkinlik_sepet.isim,
                    etkinlik_tarihi = etkinlik_sepet.etkinlik_tarihi,
                    etkinlik_saat = etkinlik_sepet.etkinlik_saat,
                    resim = etkinlik_sepet.etkinlik_resim_profil,
                    slug = etkinlik_sepet.slug,
                    # etkinlik_mekan = etkinlik_sepet.etkinlik_mekan
                )
                sepet.etkinlik_mekan.set(etkinlik_sepet.etkinlik_mekan.all()) 
                sepet.save()
                return redirect('sepet')
    return render (request, 'etkinlik-bilet.html',context)


def sepet(request):
    user = request.user
    sepet =  Sepet.objects.filter(user=user)

    # sepetiniçindeki toplam miktar ve toplam fiyatı gösterir.
    sepet_miktar = 0
    sepet_toplam_fiyat = 0
    for sepet_item in sepet:
        sepet_miktar += sepet_item.miktar
        sepet_toplam_fiyat += sepet_item.fiyat
    
    context = {
        'sepet' : sepet,
        'sepet_miktar': sepet_miktar,
        'sepet_toplam_fiyat': sepet_toplam_fiyat
    }

    return render (request,'sepet.html',context)


def sepetSil(request, etkinlik_id):
    sepet_urun = get_object_or_404(Sepet, id=etkinlik_id, user=request.user)
    sepet_urun.delete()
    return redirect('sepet')

def sepetHepsiniSil(request):
    sepet_urun = get_object_or_404(Sepet, user=request.user)
    sepet_urun.delete()
    return redirect('index')

def mekan(request, slug):
    mekan = get_object_or_404(EtkinlikMekan, slug=slug)
    etkinlik = Etkinlik.objects.filter(
        Q(etkinlik_mekan = mekan)
        )

    context ={
        'mekan' : mekan,
        'etkinlik' : etkinlik,
    }
    return render(request, 'mekan.html',context)

# footer-sayfaları-görüntüleme-foksiyonu-başlangıç
def yardim(request):
    return render(request,'yardim.html')

def satisKanal(request):
    return render(request,'saleschannel.html')

def hediyeKart(request):
    return render(request,'hediyekart.html')

def etkinlikKatılım(request):
    return render(request,'etkinlik-katılım.html')

def account(request):
    return render(request,'account.html')

def createAccount(request):
    return render(request,'createaccount.html')

def bizKimiz(request):
    return render(request,'biz-kimiz.html')

def kurumPolitikası(request):
    return render(request, 'qualitypolicies.html')

def görselMateryal(request):
    return render(request, 'görsel-materyal.html')

def bizeUlas(request):
    return render(request, 'contactus.html')

def reklamVer(request):
    return render(request, 'advertisewithus.html')

def kariyer(request):
    return render(request, 'career.html')

def sözlesmePolitika(request):
    return render(request, 'sözlesmepolitika.html')

def ttkBildirim(request):
    return render(request, 'ttk-bildirim.html')