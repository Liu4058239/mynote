from django.http import HttpResponse
from django.shortcuts import render

def show_homepage(request):
    return render(request,'homepage.html',locals())