from multiprocessing import context
from optparse import TitledHelpFormatter
from django.shortcuts import render, HttpResponse,redirect
from .models import Book
from .models import Author

def index(request):
    context={
        "all_the_books" : Book.objects.all(),
    }
    return render(request,'index.html',context)

def addbook(request):
    TITLE= request.POST['title']
    DESCRIPTION=request.POST['description']
    Book.objects.create(title=TITLE,desc=DESCRIPTION)
    return redirect('/')

def bookdesc(request,id):
    context={
       "the_book" : Book.objects.get(id=id),
       "the_authors" : (Book.objects.get(id=id)).authors.all(),
       "all_the_authors" : Author.objects.all(),
    
    }
    # print(context['the_authors'])
    return render(request,'display_book.html',context)

def selected_author(request):
    this_book=Book.objects.get(request.POST['mar'])
    id_for_author = request.POST['select1']    
    this_book.authors.add(id_for_author)
    return redirect('books/<int:id>')