from . import views
from django.urls import path

urlpatterns = [
    path('', views.root, name='root'),
    path('all_hostels/', views.all_hostels, name='all_hostels'),
    path('available_hostels/', views.available_hostels, name='available_hostels'),
    path('create_hostel/', views.create_hostel, name='create_hostel'),
    path('send_message/', views.send_message, name='send_message'),
    path('search_hostels/<str:address>/', views.search_hostels, name='search_hostels'),
    
]
