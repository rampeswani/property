from django.contrib import admin
from django.urls import path, include
from masters import views

urlpatterns = [
    path('bhk-create', views.BHKCreate, name='bhk-create'),
    path('bhk-list',views.BHKList, name='bhk-list'),
    path('masters-data',views.MasterData, name='masters-data'),


]
