from rest_framework import serializers
from goods.models import Goods, GoodsCategory


#使用rest_framework 序列化
# class GoodsSerializer(serializers.Serializer):
#
#    name = serializers.CharField(max_length=100)
#    # 点击数
#    click_num = serializers.IntegerField(default=0)
#    # 销售量
#    sold_num = serializers.IntegerField(default=0)
#    #封面，自动帮我在图片的路径前面加上media
#    goods_fron_image = serializers.ImageField(default="")
#    add_time = serializers.DateTimeField(default='')

#使用ModelSerializer,这个更加简单方便
class GoodsCategorySerializer(serializers.ModelSerializer):
   class Meta:
      #Model
      model = GoodsCategory
      #把所有的属性都用上的写法
      fields = "__all__"

#使用ModelSerializer,这个更加简单方便
class GoodsSerializer(serializers.ModelSerializer):
   category = GoodsCategorySerializer()
   class Meta:
      #Model
      model = Goods
      # fields = ('name', 'click_num', 'sold_num', 'goods_sn','goods_brief')
      #把所有的属性都用上的写法
      fields = "__all__"


class GateSerializer(serializers.ModelSerializer):

   class Meta:
      # Model
      model = GoodsCategory
      # fields = ('name', 'click_num', 'sold_num', 'goods_fron_image',"add_time")
      # 把所有的属性都用上的写法
      fields = "__all__"

class GoodsCreateSerializer(serializers.ModelSerializer):
   # category = GoodsCategorySerializer()
   class Meta:
      #Model
      model = Goods
      # fields = ('name', 'click_num', 'sold_num', 'goods_sn','goods_brief')
      #把所有的属性都用上的写法
      fields = "__all__"


