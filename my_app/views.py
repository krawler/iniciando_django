from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("olá mundo")

def home_param(request, post_id):
    return HttpResponse('Olá mundo! %s' % post_id)
