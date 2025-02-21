from django.urls import path
from home import views
urlpatterns = [
    path('',views.Home,name='home'  ),
    path('new',views.New, name='new'),
    path('property-list',views.Property_List,name='property-list'),
    path('contact', views.ContactPage , name='contact'),
    path('c',views.Contact , name='c'),
    path('detail-form', views.DetailForm , name='detail-form'),
    path('get-cities-by-state/', views.get_cities_by_state, name='get_cities_by_state'),
    path('get-locations-by-city', views.get_location_by_city , name = 'get_locations_by_city'),
    path('login',views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('admin-',views.admin,name='admin'),
    path('list-form-data',views.ListFormData, name='list-form-data'),
    path('big-index',views.Big, name='big-index'),
]
