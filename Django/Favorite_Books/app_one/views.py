from multiprocessing import context
from urllib.request import Request
from wsgiref import validate
from django.forms import EmailField
from django.shortcuts import render, HttpResponse , redirect
from .models import User
from .models import Book
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,'index.html')


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
    return redirect('/books')

def log(request):
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id']=user.id

    if bcrypt.checkpw(request.POST['pass'].encode(), user.password.encode()):
        return redirect('/books')
        
    else:
        print("password failed") 
        messages.error(request,'Please check your email and password')   
        return redirect('/') 

def out(request):
    request.session.clear()
    return redirect('/')

def suc(request):
    if 'user_id' not in request.session:
       messages.error(request,'You must log in first')
       return redirect('/')
    context={
        'this_user':User.objects.get(id=request.session['user_id']),
        'all_books':Book.objects.all().order_by('description')
    }
    return render(request,'index2.html',context)

def addbook(request,id):
    errors=Book.objects.basic_validator(request.POST)
    if len(errors)>0:
        for error in errors.values():
            messages.error(request,error)
        return redirect('/books')

    TITLE= request.POST['title']
    DESC= request.POST['desc']

    my_book = Book.objects.create(title=TITLE, description=DESC,uploaded_by=User.objects.get(id=id))
    this_user=User.objects.get(id=id)
    my_book.users_who_like.add(this_user)

    return redirect('/books')

def bookdetails(request,id):
    context={
        'this_book':Book.objects.get(id=id),
        'user_login':User.objects.get(id=request.session['user_id'])
    }
    return render(request,'index3.html',context)



def updatedesc(request,id):
    
    c = Book.objects.get(id=id)
    c.description = request.POST['text_desc']
    c.title=request.POST['text_title']
    c.save()
    context={
        'this_book':Book.objects.get(id=id),
    }
    return render(request,'index3.html',context)


def deletedesc(request,id):
    c = Book.objects.get(id=id)
    c.delete()

    return redirect('/books')

def unfavorite(request,idu,id):
    this_user=User.objects.get(id=idu)
    my_book = Book.objects.get(id=id)
    this_user.liked_books.remove(my_book)
    return redirect('/books')

def favorite(request,idu,id):
    this_user=User.objects.get(id=idu)
    my_book = Book.objects.get(id=id)
    this_user.liked_books.add(my_book)
    print(id)
    print(idu)
    return redirect('/books')

