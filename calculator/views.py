from django.shortcuts import render
from django.contrib import admin

# Create your views here.


def index(request):
    return render(request, "index.html")


def calculator(request):
    return render(request, "calculator.html")


def about_per(request):
    return render(request, "about per.html")


def contact_us(request):
    return render(request, "contact us.html")


def per_rating(request):

 #TO GET THE FULL CODE, SEND ME A MAIL AT ayushk0412@gmail.com, WITH THE SUBJECT "CODE REQUIRED"
