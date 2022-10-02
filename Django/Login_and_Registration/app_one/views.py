from multiprocessing import context
from urllib.request import Request
from wsgiref import validate
from django.forms import EmailField
from django.shortcuts import render, HttpResponse , redirect
from .models import User
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'index.html')


def make(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for error in errors.values():
            messages.error(request,error)
        return redirect('/')

    FNAME=request.POST['fname']
    LNAME=request.POST['lname']
    EMAIL=request.POST['email']
    PASS1=request.POST['pass1']
   
    pw_hash = bcrypt.hashpw(PASS1.encode(), bcrypt.gensalt()).decode() 
    print(pw_hash)      
    User.objects.create(first_name=FNAME,last_name=LNAME,email=EMAIL,password=pw_hash)
    user = User.objects.get(email=request.POST['email'])
    
    request.session['user_id']=user.id
    return redirect('/success')

def log(request):
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id']=user.id
    if user.password != request.POST['pass']:
        messages.error(request,'Please check your email and password')
        print("failed password")
        return redirect('/')
        
    else:
        print("password match")    
        return redirect('/success')

def suc(request):
    if 'user_id' not in request.session:
       messages.error(request,'You must log in first')
       return redirect('/')
    context={
        'this_user':User.objects.get(id=request.session['user_id'])
    }
    return render(request,'index2.html',context)

def suc2(request):
    request.session.clear()
    return render(request,'index.html')