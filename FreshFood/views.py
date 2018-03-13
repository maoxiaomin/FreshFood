from django.views import View
from django.shortcuts import render

from goods.models import GoodsType, Goods, Banner

class IndexView(View):
    def get(self, request):
        banners = Banner.objects.all().order_by('index')
        goods_all = Goods.objects.all()

        goodstype_all = GoodsType.objects.all()
        fruits = goodstype_all[0].goods_set.order_by('price')[:4]
        t_fruits = goodstype_all[0].goods_set.order_by('-on_click')[:2]
        # fruits = goods_all.filter(goodstype__name='新鲜水果').order_by('-price')[:4]
        # t_fruits = goods_all.filter(goodstype__name='新鲜水果').order_by('-on_click')[:3]
        context = {
            'banners': banners,
            'fruits': fruits,
            't_fruits': t_fruits
        }

        return render(request, 'index.html', context)