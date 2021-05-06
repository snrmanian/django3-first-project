from django.shortcuts import render
from random import choice

def home(request):
    return render(request,'pwgen/home.html')

def pwgen(request):
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    special="!@#$%^&*()"

    length = int(request.GET['length'])

    characters=""
    if request.GET.get('upper'):
        characters=characters + upper
    if request.GET.get('lower'):
        characters=characters + lower
    if request.GET.get('numbers'):
        characters=characters + numbers
    if request.GET.get('special'):
        characters=characters + special
    
    pw=""
    for i in range(length):
        pw=pw+choice(characters)

    return render(request,'pwgen/pwgen.html',{'result':pw,'cd':request.GET,'ab':type(request.GET)})

def about(request):
    return render(request,'pwgen/about.html')

def master(request):
    return render(request,'master.html')


    



