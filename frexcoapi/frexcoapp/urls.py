from django.urls import path
from frexcoapp.views import (RegionList, RegionDetail, FruitList, FruitDetail)

urlpatterns = [
    path('region/', RegionList.as_view()),
    path('region/<int:pk>/', RegionDetail.as_view()),
    path('fruit/', FruitList.as_view()),
    path('fruit/<int:pk>/', FruitDetail.as_view()),
]