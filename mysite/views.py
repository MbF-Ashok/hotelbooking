# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.template import loader
from models import Tables, Reservations
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect 
# Create your views here.
def home(request):
    template_var = {}
    table = Tables.objects.all()
    reserv = Reservations.objects.all()
    template_var['table'] = table
    template_var['reserv'] = reserv
    return render(request, 'mysite/home.html', template_var)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})
@csrf_exempt
def reservation(request):
    table_id = str(request.POST['val'])
    now = datetime.datetime.now()
    now_plus_1 = now + datetime.timedelta(hours = 1)
    lis = []
    for x in table_id:
        if x != ',':
            lis.append(int(x))
    booking_tables = lis
    table = Tables.objects.all()
    user_id = request.POST['user_id']
    user = User.objects.get(id=user_id)
    for tab in booking_tables:
        for a in table:
            table_val = Tables.objects.get(id=a.id)
            if a.id == tab:
                Tables.objects.filter(id=a.id).update(status=1)
                Reservations.objects.create(user_id=user,table_id=table_val,reservation_status=0,start_time=now ,end_time=now_plus_1)
    return HttpResponse('success')

@csrf_exempt
def reserv_table(request):
    table_id = str(request.POST['val'])
    table_val = Tables.objects.get(id=table_id)
    user_id = request.POST['user_id']
    now = datetime.datetime.now()
    now_plus_1 = now + datetime.timedelta(hours = 1)
    user = User.objects.get(id=user_id)
    Tables.objects.filter(id=table_id).update(status=1)
    Reservations.objects.create(user_id=user,table_id=table_val,reservation_status=0,start_time=now ,end_time=now_plus_1)
    return HttpResponse('success')


def create_table(request):
    template_var = {}
    if request.method == "POST":
        print '--------------------------------'
        first_name = request.POST['username']
        last_name = request.POST['password']
        if first_name and last_name:
            Tables.objects.create(tabel_name=first_name, tabel_capacity=int(last_name), status=0)
            return redirect('mysite:home')
    print('=============================')
    return render(request, 'mysite/create_table.html', template_var)