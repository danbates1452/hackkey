from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .password_generator import generate_secure_password

universal_context = dict()

def setup_universal_context():
    xp = 700
    xp_to_level_up = 1000
    progress_val =  round(xp / xp_to_level_up * 100, 0)
    remaining_progress_val = 100 - progress_val

    universal_context.update({
        'xp': xp,
        'xp_to_level_up': xp_to_level_up,
        'progress_val': progress_val,
        'remaining_progress_val': remaining_progress_val
    })

@csrf_exempt
def index(request):
    context = universal_context.copy()
    context.update({
        'page_name': 'index',
    })

    return render(request, 'index.html', context=context)

def login(request):
    context = universal_context.copy()
    context.update({
        'page_name': 'login',
    })
    
    return render(request, 'login.html', context=context)

def gacha(request):
    context = universal_context.copy()
    context.update({
        'page_name': 'gacha',
    })

    return render(request, 'gacha.html', context=context)

def passwords(request):
    generated_password = ""
    context = universal_context.copy()
    print(request.method)
    variable_i_want_to_output = ''
    if request.method == 'POST':
        #myvar = request.POST.get('myvar')
        print([(key, value) for key, value in request.POST.items()])
        print("test")
        if request.POST.get('my_flag') == '1':
            print("salt" + generate_secure_password)
            generated_password = generate_secure_password()
            # variable_i_want_to_output = method_i_feel_like_calling_rn()
            context.update({
                'generated_password': generated_password,
                # print(generated_password:)
            })            
    context.update({
        'page_name': 'passwords',
        'page_title': 'Password Generator',        
        'variable_i_want_to_output': variable_i_want_to_output,
    })

    return render(request, 'passwords.html', context=context)


setup_universal_context()