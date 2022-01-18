from django.urls import path
from frexcoapp.views import (index_help, RegionList, RegionDetail, FruitList, FruitDetail)

urlpatterns = [
    path('', index_help),
    path('region/', RegionList.as_view(), name="region_list"),
    path('region/<int:pk>/', RegionDetail.as_view(), name="region_detail"),
    path('fruit/', FruitList.as_view(), name="fruit_list"),
    path('fruit/<int:pk>/', FruitDetail.as_view(), name="fruit_detail"),
]