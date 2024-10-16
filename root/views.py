from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>hello nigga<h2>')

def contactus(request):
    return HttpResponse('<h2>you wanna find me nigga ?<h2>')

def aboutus(request):
    return HttpResponse('im the nigger king !')
