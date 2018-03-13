from django.contrib import admin

from .models import GoodsType, Goods, Banner


@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('goodstype', 'name', 'number', 'price', 'specs', 'on_click')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url', 'index')
