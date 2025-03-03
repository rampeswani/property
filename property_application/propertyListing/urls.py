from django.contrib import admin
from django.urls import path, include
from propertyListing import views
urlpatterns = [
  
  path('list',views.PropertyList , name='property-list'),
  path('add',views.PropertyAdd,name = 'property-add'),
  path('',views.PropertyListWeb, name='property-list-web'),
  path('load-partial',views.partial , name='partial'),

]