from unicodedata import numeric
from django.shortcuts import render, redirect
from.models import *

def Home(request):
    return render(request,'htmlfile/home.html')

def Aboutus(request):
    return render(request,'htmlfile/aboutus.html')

def Interactivemap(request):
    return render(request,'htmlfile/interactivemap.html')

def Activity(request):
    return render(request,'htmlfile/activity.html')

def Contact(request):
    return render(request,'htmlfile/contact.html')

def PathomThani(request):
    return render(request,'htmlfile/Pathom Thani.html')