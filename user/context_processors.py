from etkinlik.models import *

def kategori_context(request):
    kategori = Kategori.objects.all()
    return{'kategori' : kategori}

# def sepet_context(request):
#     user = request.user
#     sepet = Sepet.objects.filter(user=user)
    
#     # sepetteki-tüm-miktarı-görüntüler
#     sepet_miktar = 0
#     for sepet_item in sepet:
#         sepet_miktar += sepet_item.miktar
#     return{'sepet_miktar' : sepet_miktar} 