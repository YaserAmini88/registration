from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic
from .form import RegForm
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .models import formModel

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

class Register(generic.CreateView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Register, self).dispatch(request, *args, **kwargs)

    model = formModel
    form_class = RegForm
    success_url = reverse_lazy('login.html/')
    template_name = 'register.html'
    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)

def login(request):
    return render(request, 'login.html')

