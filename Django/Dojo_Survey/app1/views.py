from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return render(request, 'index.html')

def create_user(request):
    name_from_form = request.POST['name1']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    request.session['NAME']=name_from_form
    request.session['LOCATION']=location_from_form
    request.session['LANGUAGE']=language_from_form 
    request.session['COMMENT']=comment_from_form 
    return redirect('/final')

def f(request):
  return render(request, 'index2.html')