from django.shortcuts import render, HttpResponse,redirect
from .models import Show

def page_show(request):
    context={
        'all_shows':Show.objects.all()
    }
    return render(request,'all_TV_shows.html',context)

def page_add_show(request):
    return render(request,'new_show.html')

def create_show(request):
    TITLE=request.POST['title']
    NETWORK=request.POST['network']
    DATE=request.POST['date']
    DESC=request.POST['desc']
    Show.objects.create(title=TITLE,network=NETWORK,release_date=DATE,description=DESC)
    this_show=Show.objects.last()
    id_for_this_show=this_show.id  
    return redirect('/shows/'+str(id_for_this_show))

def page_desc(request,id):
    context={
        'this_show':Show.objects.get(id=id)
    }
    return render(request,'details_show.html',context)

def page_edit(request,id):
    show=Show.objects.get(id=id)
    show.release_date = show.release_date.strftime("%Y-%m-%d")
    context={
        'this_show':show
    }
    return render(request,'edit_show.html',context)
    
def update_show(request,id):
    TITLE=request.POST['title']
    NETWORK=request.POST['network']
    DATE=request.POST['date']
    DESC=request.POST['desc']
    x=Show.objects.get(id=id)
    x.title=TITLE
    x.network=NETWORK
    x.release_date=DATE
    x.description=DESC
    x.save()
    return redirect('/shows/'+str(id))

def delete_show(request,id):
    c=Show.objects.get(id=id)
    c.delete()
    return redirect('/shows')
