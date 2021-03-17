from django.contrib import admin
from django.urls import path, re_path,include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from goods.view_request_response import GoodsListViewRequestResponse

from goods.views import GoodsListViewSet,GoodsListView  # , GateView

#实例化默认路由
router = routers.DefaultRouter()
#注册商品列表
router.register(r'goods', GoodsListViewSet, basename='goods')
router.register(r'goods2', GoodsListView, basename='goods2')

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^jwt-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    re_path(r'^docs/', include_docs_urls(title="my store")),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # re_path('goods/', GoodsListView.as_view(), name="goods_list"),
    # re_path('^goods/', GoodsListViewSet.as_view(), name="goods_list"),
    re_path(r'^goods_test/$',GoodsListViewRequestResponse.as_view(),name="goods_list_test"),
    # re_path('^goods_set/', GoodsListViewSet, name="goods_list"),
    # re_path('gates/', GateView.as_view(), name="goods_list"),
]
