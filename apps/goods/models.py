from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class GoodsType(models.Model):
    name= models.CharField('商品类别', max_length=20)
    zjm = models.CharField('助记码', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = '商品类别信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Goods(models.Model):
    goodstype = models.ForeignKey(GoodsType, on_delete=models.CASCADE,verbose_name='所属类别')
    name = models.CharField('品名', max_length=20)
    number = models.IntegerField('数量', default=0)
    profile =models.CharField('简介', max_length=100)
    desc = RichTextField('商品描述')
    image = models.ImageField('商品图片', max_length=100, upload_to='goods/%Y/%m', default='goods/default.png')
    price = models.DecimalField('价格',max_digits=6, decimal_places=2)
    specs = models.CharField('规格', max_length=20)
    on_click = models.IntegerField('点击数', default=0)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', max_length=100, upload_to='banner/%Y/%m', default='banner/default.png')
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('显示顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title