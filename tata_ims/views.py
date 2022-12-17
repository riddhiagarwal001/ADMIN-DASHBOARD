from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':' HOME PAGE'
    }
    return render(request,"index.html",data) 

def aboutUs(request):
    return HttpResponse("<b>Welcome to Tata IMS</b>")     #optional

