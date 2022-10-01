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

def selected_author(request,id):
    
    this_author=Author.objects.get(id=request.POST['select_add'])
    print(this_author)
    this_book=Book.objects.get(id=id)  
    print(this_book)
    this_book.authors.add(this_author)

    context={
       "the_book" : Book.objects.get(id=id),
       "the_authors" : (Book.objects.get(id=id)).authors.all(),
       "all_the_authors" : Author.objects.all(),
    }
    return render(request,'display_book.html',context)

#########
def index2(request):
    context={
        "all_the_authors" : Author.objects.all(),
    }
    return render(request,'index2.html',context)

def addauthor(request):
    FNAME= request.POST['fname']
    LNAME= request.POST['lname']
    NOTE= request.POST['note']
    Author.objects.create(first_name=FNAME,last_name=LNAME,notes=NOTE)
    return redirect('/authors')

def authordesc(request,id):
    context={
       "the_author" : Author.objects.get(id=id),
       "the_books" : (Author.objects.get(id=id)).books.all(),
       "all_the_books" : Book.objects.all(),
    }
    print(context['the_author'])
    return render(request,'display_author.html',context)

def selected_book(request,id):
    
    this_book=Book.objects.get(id=request.POST['select_add2'])
    this_author=Author.objects.get(id=id)  
    this_author.books.add(this_book)
    context={
       "the_author" : Book.objects.get(id=id),
       "the_books" : (Author.objects.get(id=id)).books.all(),
       "all_the_books" : Book.objects.all(),
    }

    return render(request,'display_author.html',context)