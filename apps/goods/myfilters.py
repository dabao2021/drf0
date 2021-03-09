from django_filters import rest_framework as filter
from .models import Goods


#商品的过滤器
class GoodsFilter(filter.FilterSet):
   #最低价格
   min_price = filter.NumberFilter(field_name="shop_price", lookup_expr='gte')
   #最大价格
   max_price = filter.NumberFilter(field_name="shop_price", lookup_expr='lte')

   name = filter.CharFilter(field_name="name",lookup_expr='icontains')
# 包含 icontains

   class Meta:
      model = Goods
      fields = [ 'min_price', 'max_price', 'name']