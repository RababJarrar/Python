
from django.shortcuts import render, HttpResponse,redirect
from.models import User
def index(request):
    context ={
        "all_the_users": User.objects.all()
    }
    return render(request,'index.html',context)

def add(request):
    User.objects.create(Name=(request.POST['name1']+' '+request.POST['name2']),Email=request.POST['email'],Age=request.POST['age'])
    return redirect('/')