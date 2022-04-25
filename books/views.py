from django.http import HttpResponse
from django.shortcuts import render
from .models import Books
# Create your views here.
def home(request):
    return render(request, 'index.html')

def books(request):
    books = Books.objects.all()   
    '''
    context = {
        'books':books,
        'avail':availabality
        }
    result.append(context)'''

    return render(request, 'books.html', {'books':books})