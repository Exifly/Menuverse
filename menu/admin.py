from django.contrib import admin
from .models import Item, Menu, Allergene, FeedBack

# Register your models here.


class AllergenInline(admin.TabularInline):
    model = Allergene

class AllergeneAdmin(admin.ModelAdmin):
   list_display = ['tipo']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu', 'nome','descrizione', 'visualizza',  'prezzo', 'photo']
    inlines = [
        AllergenInline,
    ]

class ItemInline(admin.TabularInline):
    model = Item


class MenuAdmin(admin.ModelAdmin):
   list_display = ['nome', 'visualizza']
   inlines = [
       ItemInline,
   ]


class FeedBackAdmin(admin.ModelAdmin):
   list_display = ['nome', 'messaggio']


admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Allergene, AllergeneAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Menu, MenuAdmin)

