from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return home(request)

def home(request):
    context = {
        'message': 'have fun',
    }
    return render(request, 'home.html', context=context)