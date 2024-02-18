from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .password_generator import generate_secure_password, pass_credentials_to_database
from hackkey.models import Users, Entries, PremiumFeatures, GachaRewards

universal_context = dict()

def setup_universal_context():
    test_user = Users.objects.get_or_create(id=1)[0]
    selected_theme = test_user.selected_theme
    
    test_user.selected_theme = 'blue'
    test_user.save()
    #todo: implement a way for users to choose a rewarded theme

    xp = 700
    xp_to_level_up = 1000
    progress_val =  round(xp / xp_to_level_up * 100, 0)
    remaining_progress_val = 100 - progress_val

    universal_context.update({
        'selected_theme': selected_theme,
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
    if request.method == 'POST':
        # if request.POST.get('btn_generate_password') == '1':
        if 'btn_generate_password' in request.POST:
            generated_password = generate_secure_password()
            usr_username = request.POST.get('inp_email')
            context.update({
            'generated_password': generated_password,
            'email_address': usr_username,
            })
        elif 'btn_store_credentials' in request.POST:
            usr_username = request.POST.get('inp_email')
            usr_password = request.POST.get('inp_password')
            context.update({
            'generated_password': generated_password,
            'email_address': usr_username,
            })
            

            print(f"User stored: {usr_username}, Pass stored: {usr_password}")
            pass_credentials_to_database(1, usr_username, usr_password)

        # a@a.com
         
        # elif request.POST.get('btn_store_credentials') == '2':
        #     usr_username = request.POST.get('exampleInputEmail1')
        #     usr_password = request.GET.get('exampleInputPassword1')
        #     # pass_credentials_to_database(1, usr_username, usr_password)

    context.update({
        'page_name': 'passwords',
        'page_title': 'Password Generator',        
    })

    return render(request, 'passwords.html', context=context)

setup_universal_context()