from django.shortcuts import render, HttpResponse,redirect  
import random
gussedNumber = random.randint(1, 100)

def index(request):
    
    return render(request,'index.html')

def root(request):
    # request.session['guess'] = gussedNumber
    enterNumber = request.POST['user_number']

    if (int(enterNumber)==int(gussedNumber)):
       request.session['result'] = 'correct' 

    elif ((int(enterNumber)>(int(gussedNumber)+10)) or (int(enterNumber)<(int(gussedNumber)-10))):
        request.session['result'] = 'Too High!'

    else:
        request.session['result'] = 'Too Low!'
    return render(request,'index2.html')

