from multiprocessing import context
from urllib.request import Request
from wsgiref import validate
from django.forms import EmailField
from django.shortcuts import render, HttpResponse , redirect
from .models import User
from .models import Message
from .models import Comment
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
   
    pw_hash = bcrypt.hashpw(request.POST['pass1'].encode(), bcrypt.gensalt()).decode() 
    print(pw_hash)      
    User.objects.create(first_name=FNAME,last_name=LNAME,email=EMAIL,password=pw_hash)
    user = User.objects.get(email=request.POST['email'])
    
    request.session['user_id']=user.id
    return redirect('/success')

def log(request):
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id']=user.id

    if bcrypt.checkpw(request.POST['pass'].encode(), user.password.encode()):
        return redirect('/success')
         
    else:
        print("password failed") 
        messages.error(request,'Please check your email and password')   
        return redirect('/') 
########################################################
def suc(request):
    if 'user_id' not in request.session:
       messages.error(request,'You must log in first')
       return redirect('/')
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'all_user':User.objects.all()
    }
    return render(request,'index2.html',context)
########################################################
def out(request):
    request.session.clear()
    return redirect('/')

########################################################

def post_m(request,id):
    MESS= request.POST['mess']
    my_message = Message.objects.create(message=MESS, user=User.objects.get(id=id))
    return redirect('/success')

def post_c(request,u_id,m_id):
    COMM= request.POST['comm']
    my_comment = Comment.objects.create(comment=COMM,message=Message.objects.get(id=m_id), user=User.objects.get(id=u_id))
    return redirect('/success')

