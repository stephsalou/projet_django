import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from sport.sportForm import UserForm
from django.shortcuts import render, redirect



# Create your views here.
def affichage(request):
    return render(request, 'public/inscription.html')


@require_http_methods(['POST'])
def sport_register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            errors=[user_form.errors,]
            return render(request, 'public/inscription.html', {'erreur':errors})
    return render(request,'public/inscription.html')


@require_http_methods(['POST'])
def sport_login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    try:
        user = authenticate(username=username, password=password)
    except:
        raise Exception('nom d\'utilisateur ou mot de pass erroner')
    if user is not None:
        login(request, user)
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))
        else:
            return redirect('index')
    else:
        return redirect('register_login')


@login_required(login_url='register_login')
def sport_logout(request):
    logout(request)
    return redirect('register_login')
