
from django.shortcuts import render, HttpResponse,redirect
from.models import Dojo
from.models import Ninja
def index(request):
    context ={
        "all_the_dojos": Dojo.objects.all(),
    }
                                                        # for dojo in context['all_the_dojos']:
                                                        #     print(dojo.ninjas.all())
    return render(request,'index.html',context)

def adddojo(request):
    NAME=request.POST['name']
    CITYY=request.POST['city']
    STATE=request.POST['state']
    Dojo.objects.create(name=NAME,city=CITYY,state=STATE)
    return redirect('/')

def addninja(request):
    FNAME=request.POST['fname']
    LNAME=request.POST['lname']
    DOJO_ID=request.POST['dojo_id']
    Ninja.objects.create(first_name=FNAME,last_name=LNAME,dojo=Dojo.objects.get(id=DOJO_ID))
    return redirect('/')