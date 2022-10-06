from multiprocessing import context
from urllib.request import Request
from wsgiref import validate
from django.forms import EmailField
from django.shortcuts import render, HttpResponse , redirect
from .models import User
from .models import Tree
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'login_page.html')

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
    return redirect('/dashboard')

def log_in(request):
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id']=user.id

    if bcrypt.checkpw(request.POST['pass'].encode(), user.password.encode()):
        return redirect('/dashboard')
        
    else:
        print("password failed") 
        messages.error(request,'Please check your email and password')   
        return redirect('/') 
        
def log_out(request):
    request.session.clear()
    return redirect('/')

def page_success(request):
    if 'user_id' not in request.session:
       messages.error(request,'You must log in first')
       return redirect('/')
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'all_trees':Tree.objects.all()
    }
    return render(request,'main_page.html',context)

def page_add_tree(request):
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        }
    return render(request,'add_page.html',context)



def add_tree(request,id):
    errors=Tree.objects.basic_validator(request.POST)
    if len(errors)>0:
        for error in errors.values():
            messages.error(request,error)
        return redirect('/dashboard')
    USER=User.objects.get(id=id)
    SP=request.POST['species']
    LOCA=request.POST['location']
    RE=request.POST['reason']
    DA=request.POST['date']
    id_for_user=id
    Tree.objects.create(species=SP,user=USER,location=LOCA,reason=RE,created_at=DA)
    return redirect('/dashboard')

def show_tree(request):
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'my_trees':Tree.objects.all(),
        }
    return render(request,'mytree_page.html',context)

def delete_tree(request,id):
    c = Tree.objects.get(id=id)
    c.delete()
    return redirect('/user/account')

def page_edit_tree(request,id):
    tree=Tree.objects.get(id=id)
    tree.created_at = tree.created_at.strftime("%Y-%m-%d")
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'this_tree':Tree.objects.get(id=id),
        }
    return render(request,'edit_page.html',context)

def update_tree(request,id):
    errors=Tree.objects.basic_validator(request.POST)
    if len(errors)>0:
        for error in errors.values():
            messages.error(request,error)
        return redirect('/user/account')
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'this_tree':Tree.objects.get(id=id),
        }
    c = Tree.objects.get(id=id)
    c.species = request.POST['species'] 
    c.location = request.POST['location'] 
    c.reason  = request.POST['reason'] 
    c.created_at = request.POST['date'] 
    c.save()
    return redirect('/user/account')


def detailes(request,id):
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'this_tree':Tree.objects.get(id=id)
        }
    return render(request,'show.html',context)