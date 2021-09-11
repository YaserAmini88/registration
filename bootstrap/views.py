from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    #template = loader.get_template('dashboard.html')
    return render(request, 'dashboard.html')

def user(request):
    return render(request, 'user.html')

def table(request):
    return render(request, 'table.html')

def typo(request):
    return render(request, 'typography.html')

def icons(request):
    return render(request, 'icons.html')

def maps(request):
    return render(request, 'maps.html')

def notifications(request):
    return render(request, 'notifications.html')

def dashboard(request):
    return render(request, 'dashboard.html')
