from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import format_html
from .models import *

class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
    readonly_fields = ('slug',)
    list_display = ('tree_actions', 'something',)
    list_display_links = ('something',)

    def something(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.isim,  # Or whatever you want to put here
        )

class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ('isim','kategori','etkinlik_tarihi','stok','hot_ticket','carousel_index','one_cikan_index','tum_tr','muzik_index','sahne_index','spor_index','aile_index',)
    readonly_fields = ("slug",)
    list_filter = ('kategori','etkinlik_tarihi',)
    list_editable = ('stok','hot_ticket','carousel_index','one_cikan_index','tum_tr','muzik_index','sahne_index','spor_index','aile_index',)
    search_fields = ['isim','kategori__isim']




class EtkinlikMekanAdmin(admin.ModelAdmin):
    list_display = ('isim','sehir',)
    search_fields = ['isim','sehir']

    
class SepetAdmin(admin.ModelAdmin):
    list_display = ('user','isim','miktar')
    readonly_fields = ("slug",)


    
admin.site.register(Kategori, MyDraggableMPTTAdmin)
admin.site.register(Etkinlik, EtkinlikAdmin)
admin.site.register(EtkinlikMekan, EtkinlikMekanAdmin)
admin.site.register(Sepet, SepetAdmin)
admin.site.register(Musteri)
admin.site.register(Adres)