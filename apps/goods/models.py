from datetime import datetime

from django.db import models

#商品类别
class GoodsCategory(models.Model):

    name=models.CharField(default='',max_length=30,verbose_name='类别名',help_text='类别名')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#商品类
class Goods(models.Model):
    """    商品    """
    goods_sn=models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name=models.CharField(max_length=100, verbose_name="商品名")
    sold_num=models.IntegerField(default=0, verbose_name="商品销售量")

    goods_num=models.IntegerField(default=0, verbose_name="库存数")
    shop_price=models.FloatField(default=0, verbose_name="本店价格")
    goods_brief=models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_front_iamge = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name="商品类别",on_delete=models.SET_NULL)
    # fav_num=models.IntegerField(default=0, verbose_name="收藏数")
    # click_num=models.IntegerField(default=0, verbose_name="点击数")
    # goods_desc = models.TextField(max_length=500, verbose_name="内容")
    # market_price = models.FloatField(default=0, verbose_name="市场价格")
    # ship_free=models.BooleanField(default=True, verbose_name="是否承担运费")
    #
    # is_new=models.BooleanField(default=False, verbose_name="是否新品")
    # is_hot=models.BooleanField(default=False, verbose_name="是否热销")
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['id']
        
    def __str__(self):
        return self.name