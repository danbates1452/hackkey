from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .password_generator import generate_secure_password
from hackkey.models import Users, Entries, PremiumFeatures, GachaRewards

universal_context = dict()
test_user = Users.objects.get_or_create(id=1)[0]

def setup_universal_context():
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
    rolls_owned = test_user.rolls_owned
    from hackkey.gacha import roll
    context = universal_context.copy()
    new_roll = 10
    if request.method == "GET":
        new_roll == 10
    if request.method == 'POST':
        if request.POST.get('btnRoll') == 1:
            new_roll = roll()
        new_roll = roll()
        if rolls_owned > 0:
            rolls_owned -= 1
            test_user.rolls_owned = rolls_owned
            test_user.save()

    #if request.method == 'POST':
    #    if request.POST.get('value') == 1:
    #         print("CCCCCCCC")
    #         new_roll = roll()
    #         print("New Roll: " + new_roll)
    context.update({
        'rolls_owned': rolls_owned,
        'page_name': 'gacha',
        'roll_outcome': new_roll,
        #'button_roll': new_roll,
    })

    return render(request, 'gacha.html', context=context)

def passwords(request):
    generated_password = ""
    context = universal_context.copy()
    if request.method == 'POST':
        if request.POST.get('btn_generate_password') == '1':
            generated_password = generate_secure_password()
            context.update({
                'generated_password': generated_password,
            })            
    context.update({
        'page_name': 'passwords',
        'page_title': 'Password Generator',        
    })

    return render(request, 'passwords.html', context=context)

setup_universal_context()