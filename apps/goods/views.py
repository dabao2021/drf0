from django.shortcuts import render
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
# from django.views.generic import View
from django.views import View
from goods import models
from rest_framework import status, serializers

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

# from rest_framework import mixins
# from rest_framework import generics
# #提供增删改查
# class GoodsListView(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
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
class GoodsListPagination(PageNumberPagination):
   page_size = 1
   page_size_query_param = 'page_size'
   max_page_size = 3



class GoodsListView(generics.ListAPIView):
   """
   返回商品列表
   """
   #得到所有的商品
   queryset = models.Goods.objects.all()
   #序列化器
   serializer_class = GoodsSerializer
   pagination_class = GoodsListPagination # 列表个性化


#ListAPIView已经实现了get方法
class GateView(generics.ListAPIView):
   """
   返回商品列表
   """
   #得到所有的商品
   queryset = models.GoodsCategory.objects.all()
   #序列化器
   serializer_class = GateSerializer

