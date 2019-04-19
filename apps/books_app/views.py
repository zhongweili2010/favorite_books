from django.shortcuts import render,HttpResponse,redirect
from .models import Book
from ..login_registration_app.models import User
from django.contrib import messages
# Create your views here.
def books(request):
    if 'name' in request.session:
        print(request.session['name'])
        context={
            'name':request.session['name'],
            'user_id':request.session['id'],
            'all_books': Book.objects.all(),
            'the_user':User.objects.get(id=request.session['id']),
        }

        return render(request,"books_app/index.html",context)
    else:
        return HttpResponse('please log in')

def detail(request,number):
    if ('name' in request.session) and ('id' in request.session):
        print('now in book detail page')
        
        context={
            'user_id':request.session['id'],
            'name':request.session['name'],
            # 'books':Book.objects.all(),
            'the_book':Book.objects.get(id=number),
            'this_user':User.objects.get(id=request.session['id']),
        }
        return render(request,"books_app/detail.html",context)
    else:
        return HttpResponse('go log in')


def add_book(request):
    if request.method=='POST' and ('name' in request.session) and ('id' in request.session):
        print('now in add book route')
        errors=Book.objects.validate(request.POST)
        if len(errors)==0:
            this_guy=User.objects.get(id=request.session['id'])
            this_book=Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],creater=this_guy)
            this_book.favorites.add(this_guy)

            return redirect(f"/books/{this_book.id}")
        else:
            for key,value in errors.items():
                messages.info(request,value,extra_tags=key)
            return redirect('/books')
    else:
        return HttpResponse('not logged in')

def add_fav(request,number):
    if request.method=='GET' and ('name' in request.session) and ('id' in request.session):
        this_book=Book.objects.get(id=number)
        this_guy=User.objects.get(id=request.session['id'])
        this_book.favorites.add(this_guy)
        print(f"added book{this_book.id} to user {this_guy.id}")
        return redirect(f"/books")
    else:
        return HttpResponse('not logged in')


def unfav(request,number):
    if request.method=='GET' and ('name' in request.session) and ('id' in request.session):
        this_book=Book.objects.get(id=number)
        this_guy=User.objects.get(id=request.session['id'])
        this_book.favorites.remove(this_guy)
        print(f"removed book{this_book.id} to user {this_guy.id}")
        return redirect(f"/books/{number}")
    else:
        return HttpResponse('not logged in')

def update_book(request):
    if request.method=='POST' and ('name' in request.session) and ('id' in request.session):
        errors=Book.objects.validate(request.POST)
        if len( errors )>0:
            for key,value in errors.items():
                messages.info(request,value,extra_tags=key)
        else:
            this_book=Book.objects.get(id=request.POST['book_id'])
            this_book.title=request.POST['title']
            this_book.desc=request.POST['desc']
            this_book.save()

            print(f"updated book{request.POST['book_id']}")
        return redirect(f"/books/{request.POST['book_id']}")
    else:
        return HttpResponse('not logged in')


def myFav(request):
    if request.method=="GET" and ('name' in request.session) and ('id' in request.session):
        this_user=User.objects.get(id=request.session['id'])
        
        context={
            "my_favs":this_user.fav_books.all,

        }

        print(" this user is",context['my_favs'])

        return render(request,"books_app/myFav.html",context)



    else:
        return HttpResponse('not logged in')