
from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def root_method(request):
    return redirect('blogs/')

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')


def show(request,number):
    context = {
        "num": number,
    }
    return render(request,'index.html',context)   
    
def edit(request,number):
    context = {
        "num": number,
    }
    return render(request,'index2.html',context)  


def destroy(request,number):
    return redirect('/blogs')