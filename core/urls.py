from django.urls import path
from core import views

urlpatterns = [
    path('',views.index,name='index'),

    path('car',views.car,name='car'),
    path('car_single/<int:id>/',views.car_single,name='car_single'),
    path('contact',views.contact,name='contact'),
    path('car_book',views.car_book,name='car_book'),
    path('pricing',views.pricing,name='pricing'),
    path('add_car/',views.add_car,name='add_car'),


]