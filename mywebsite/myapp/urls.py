from django.urls import path
from .views import * 

urlpatterns = [
    path('',Home, name='homepage'),
    path('aboutus/',Aboutus, name='aboutuspage'),
    path('interactivemap/',Interactivemap, name='mappage'),
    path('activity/',Activity, name='activitypage'),
    path('contact/',Contact, name='contactpage'),
    path('PathomThaini/',PathomThani, name='PathomThaniPage')
]