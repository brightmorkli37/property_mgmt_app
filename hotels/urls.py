from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('properties/', views.properties, name='properties'),
    path('about-Us/', views.aboutUs, name='about'),
    path('contact-Us/', views.contactUs, name='contact'),
]