from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listcreate/', views.AdvertisementList.as_view(), name='create_ad'),
    path('listcreate/<int:pk>/', views.AdvertisementDetail.as_view()),

]