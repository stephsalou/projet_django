# from thesportsdb import thesportsdb

from django.shortcuts import render
# Create your views here.

def affichage(request):
    title='the ISO NAN PLAYEUR'
    return render(request,'public/acceuil.html',{'title':title})
