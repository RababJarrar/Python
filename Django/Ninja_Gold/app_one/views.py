
from django.shortcuts import render, HttpResponse,redirect
import random
from time import localtime, strftime
def root(request):
    if 'gold' not in request.session:
            request.session['gold']=0
            request.session['logs']=[]
    return render(request,'index.html')



def process(request):
    if 'which_form' in request.POST:   
        earn= random.randint(-50,50) if request.POST['which_form']=="quest" else random.randint(10,20)
        status='earn' if earn>=0 else 'loose'
        current_log = {
            "status": "earn" if earn>=0 else "loose",
            "message":(f"you enterd a {request.POST['which_form']} and {status}{earn} gold.({strftime('%b %d, %Y  %I:%M %p' , localtime())})"),
        }
        request.session['gold']+= earn
        request.session['logs'].append(current_log)
        request.session.save()
    return redirect('/')