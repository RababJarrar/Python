from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect  
import random


def index(request):
    gussedNumber = random.randint(1, 100)
    request.session['guess'] = gussedNumber
    context = {
        'Num' : gussedNumber
    }
    return render(request,'index.html')

def root(request):
    gussedNumber = request.session['guess'] 
    enterNumber = request.POST['user_number']

    if (int(enterNumber)==int(gussedNumber)):
       request.session['result'] = 'correct' 

    elif ((int(enterNumber)>(int(gussedNumber)))):
        request.session['result'] = 'Too High!'

    else:
        request.session['result'] = 'Too Low!'
    return redirect('/')

