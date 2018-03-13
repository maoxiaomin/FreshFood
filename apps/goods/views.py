from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .models import Goods, GoodsType

# Create your views here.

class DetailView(View):
    def get(self, request, id):
        goods = Goods.objects.get(id=id)
        return render(request, 'goods/detail.html', {'goods':goods})

class ListView(View):
    def get(self, request, type, p_number=1):
        px = request.GET.get('px', '')
        goodstype = GoodsType.objects.get(zjm=type)
        all_goods = goodstype.goods_set.all()
        new_goods = all_goods.order_by('-id')[:2]
        if px == 'jg':
            all_goods = all_goods.order_by('-price')
        if px == 'rq':
            all_goods = all_goods.order_by('-on_click')

        # 分页
        pag = Paginator(all_goods, 15)
        p = pag.page(p_number)

        context = {
            'name': goodstype.name,
            'zjm': goodstype.zjm,
            'all_goods': all_goods,
            'new_goods': new_goods,
            'px': px,
            'p':p
        }

        return render(request, 'goods/list.html', context)
