from django.shortcuts import render, HttpResponse,redirect  
import random

def index(request):
    return render(request,'index.html')

def root(request):
    gussedNumber = random.randint(1, 100)
    request.session['guess'] = gussedNumber
    enterNumber = request.Post['user_number']

    if (enterNumber==gussedNumber):
       request.session['result'] = 'correct' 

    elif ((enterNumber>gussedNumber+10) or (enterNumber<gussedNumber-10)):
        request.session['result'] = 'Too High!'

    else:
        request.session['result'] = 'Too Low!'

    return render(request,'index.html')


