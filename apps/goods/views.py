from django.shortcuts import render
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
# from django.views.generic import View
from django.views import View
from goods import models
from rest_framework import status, serializers, viewsets

from goods.models import Goods
from goods.myfilters import GoodsFilter
from goods.serializer import GoodsSerializer, GateSerializer, GoodsCategorySerializer


# 用通常的方法实现
# class GoodsListView(View):
#    def get(self,request):
#       #返回前所有商品的前10条数据
#       goods_list = Goods.objects.all()[:10]
#       # json_list = []
#       # print(goods_list)
#       # for goods in goods_list:
#       #    json_item = {}
#       #    json_item["name"] = goods.name
#       #    json_item["market_price"] = goods.market_price
#       #    json_item["sold_num"] = goods.sold_num
#       #    # json_item["add_time"] = goods.add_time#该行代码报错
#       #
#       #    json_list.append(json_item)
#       #
#       # from django.http import HttpResponse
#       # import json
#       #
#       # print(type(json_list))
#       # #转换成字符串
#       # content = json.dumps(json_list)
#       # #str
#       # print(type(content))
#       # #，在转换成json
#       # return HttpResponse(content,"application/json")#,charset='ASCII'
#       Serializer=GoodsSerializer(goods_list,many=True)

# 用序列化器实现
# class GoodsListView(APIView):
#    def get(self, request, format=None):
#       goods_list = models.Goods.objects.all()[:10]
#       serializer = GoodsSerializer(goods_list, many=True)
#       return Response(serializer.data)
#
#    def post(self, request, format=None):
#       serializer = GoodsSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GateView(APIView):
#     def get(self, request, format=None):
#         goods_list = models.GoodsCategory.objects.all()[:10]
#         serializer = GoodsCategorySerializer(goods_list, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsCategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import mixins
from rest_framework import generics
# #提供增删改查
# CreateModelMixin  --提交数据，注册用户的时候
# ListModelMixin     ---get和list方法关联起来，在list把数据进行序列化
# RetrieveModelMixin  ---得到某个商品具体的信息，在后面商品的详情页面使用
# UpdateModelMixin   ----部分更还是全部更新
# DestroyModelMixin  ---删除某条数据用到
# class GoodsListView(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                     mixins.DestroyModelMixin,
#                     mixins.UpdateModelMixin,
#                   generics.GenericAPIView):
#     queryset = models.Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


from rest_framework import generics

# 列表个性化
# class GoodsListPagination(PageNumberPagination):
#    page_size = 2
#    page_size_query_param = 'page_size'
#    page_query_param = "p"  # 页的字段
#    # 最大返回100条
#    max_page_size = 100


#
# class GoodsListView(generics.ListAPIView):
#    """
#    返回商品列表
#    """
#    #得到所有的商品
#    queryset = models.Goods.objects.all()
#    #序列化器
#    serializer_class = GoodsSerializer
#    pagination_class = GoodsListPagination # 列表个性化


#ListAPIView已经实现了get方法
class GateView(generics.ListAPIView):
   """
   返回商品列表
   """
   #得到所有的商品
   queryset = models.GoodsCategory.objects.all()
   #序列化器
   serializer_class = GateSerializer

from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from .models import Goods
from .serializer import GoodsSerializer
from rest_framework import generics
from rest_framework import viewsets

class GoodsListPagination(PageNumberPagination):
   #默认返回10条
   page_size = 2
   #每页返回多少条的参数变量
   page_size_query_param = 'page_size'
   page_query_param = "p"#页的字段
   #最大返回100条
   max_page_size = 100

#GenericViewSet
class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
   """
   返回商品列表
   """
   #得到所有的商品
   queryset = Goods.objects.all()
   #序列化期
   serializer_class = GoodsSerializer
   #添加分页配置,settings.py就可以省略了
   pagination_class = GoodsListPagination

   filter_backends = (DjangoFilterBackend,)
   # filter_fields = ('name', 'shop_price')
   filter_class = GoodsFilter
   #加上过滤条件
   # def get_queryset(self):
   #    #价格大于100的
   #    return Goods.objects.filter(name='香蕉')#(shop_price__gte=1,shop_price__lte=6)
   # def get_queryset(self):

# 得到所有的数据，但是并不是一下子全部取出来
#       queryset = Goods.objects.all()
#       # 大于或者等于的值
#       min_price = self.request.query_params.get("min_price", 0)
#       if min_price:
#          queryset = queryset.filter(shop_price__gt=int(min_price))
#       # 价格大于100的
#       return queryset


