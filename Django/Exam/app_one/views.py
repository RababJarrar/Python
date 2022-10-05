from multiprocessing import context
from urllib.request import Request
from wsgiref import validate
from django.forms import EmailField
from django.shortcuts import render, HttpResponse , redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'login_page.html')

def make_register(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for error in errors.values():
            messages.error(request,error)
        return redirect('/')
    FNAME=request.POST['fname']
    LNAME=request.POST['lname']
    EMAIL=request.POST['email']
    pw_hash = bcrypt.hashpw(request.POST['pass1'].encode(), bcrypt.gensalt()).decode() 
    print(pw_hash)      
    User.objects.create(first_name=FNAME,last_name=LNAME,email=EMAIL,password=pw_hash)
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id']=user.id
    return redirect('/success')

def log_in(request):
    user = User.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['pass'].encode(), user.password.encode()):
        return redirect('/success')   
    else:
        print("password failed") 
        messages.error(request,'Please check your email and password')   
        return redirect('/') 

def log_out(request):
    request.session.clear()
    return redirect('/')
############################################################
def show_main_page(request):
    if 'user_id' not in request.session:
       messages.error(request,'You must log in first')
       return redirect('/')
    context={
        'this_user':User.objects.get(id=request.session['user_id'])
    }
    return render(request,'main_page.html',context)
