from . import views
from django.urls import path

urlpatterns = [
    path('', views.root, name='root'),
    path('all_hostels', views.all_hostels, name='all_hostels'),
    path('available_hostels', views.available_hostels, name='available_hostels'),
    path('create_hostel', views.create_hostel, name='create_hostel'),
    
]
