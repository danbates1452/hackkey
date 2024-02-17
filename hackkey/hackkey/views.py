from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    context = {
        'message': 'index',
    }
    return render(request, 'index.html', context=context)

def login(request):
    context = {
        'message': 'login',
    }
    
    return render(request, 'login.html', context=context)