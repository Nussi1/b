from django.contrib import admin
from django.urls import path
from . import views
from .views import index, IndexDetail, index_detail

urlpatterns = [
    path('', index, name='home'),
    path('ad/<int:pk>', IndexDetail.as_view(), name='ad_detail'),
    path('ad/<int:pk>', index_detail, name='ad_detail'),
    path('create/', views.create_ad_view, name='create_ad'),
]