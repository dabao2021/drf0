from django.contrib import admin
from django.urls import path, re_path,include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListView, GateView

router = routers.DefaultRouter()
# router.register(r'goods', GoodsListView, basename='goods')


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/', include_docs_urls(title="my store")),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # re_path('goods/', GoodsListView.as_view(), name="goods_list"),
    re_path('goods/', GoodsListView.as_view(), name="goods_list"),
    re_path('gates/', GateView.as_view(), name="goods_list"),

]
