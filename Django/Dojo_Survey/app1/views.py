from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return render(request, 'index.html')

def create_user(request):
    name_from_form = request.POST['name1']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    context={
        "n": name_from_form ,
        "lo": location_from_form,
        "la":language_from_form,
        "co":comment_from_form
        }
    return render(request, 'index2.html',context)

# def create_user(request):
#     name_from_form = request.POST['name1']
#     location_from_form = request.POST['location']
#     language_from_form = request.POST['language']
#     comment_from_form = request.POST['comment']
#     context={
#         "n": name_from_form ,
#         "lo": location_from_form,
#         "la":language_from_form,
#         "co":comment_from_form
#         }
#     return redirect("/success")

# def success(request):
#     return render(request,'index2.html')