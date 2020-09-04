from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('calculator/', views.calculator, name="calculator"),
    path('result/', views.per_rating, name="result"),
    path('about_per/', views.about_per, name="about_per"),
    path('contact_us/', views.contact_us, name="contact_us"),

]
