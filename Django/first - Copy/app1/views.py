
from multiprocessing import context
from django.shortcuts import redirect, render,HttpResponse

# def index(request):
#     if request.method == "GET":
#         print(request.GET)
#     if request.method == "POST":
#         print(request.POST)
#     return render(request,'index.html')

# def index2(request):
#     if request.method == "GET":
#         print(request.GET)
#     if request.method == "POST":
#         print(request.POST)
#     return redirect('/')


def index(request):
    return render(request,"index.html")
        
def create_user(request):
    # context={
    #     'name_from':request.POST['name']
    # }
    request.session['N'] = request.POST['name']
    print(request.session['N'])
    return render(request,"index.html")

