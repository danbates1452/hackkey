from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    context = {
        'page_name': 'index',
    }
    return render(request, 'index.html', context=context)

def login(request):
    context = {+
        'page_name': 'login',
    }
    
    return render(request, 'login.html', context=context)

def gacha(request):
    context = {
        'page_name': 'gacha',
    }
    return render(request, 'gacha.html', context=context)

def passwords(request):
    context = {
        'page_name': 'passwords',
    }
    return render(request, 'passwords.html', context=context)