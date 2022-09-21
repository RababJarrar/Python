
# from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect

def index(request):
    if 'visits' not in request.session:
        request.session['visits']=0
    else:
        request.session['visits']+=1

    return render(request,'index.html')

def destroy(request):
    del request.session['visits']
    return redirect('/')
