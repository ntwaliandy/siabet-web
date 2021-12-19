from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


def board(request):
    return render(request, 'board.html')


def suggest(request):
    return render(request, 'suggest.html')


def requests(request):
    return render(request, 'requests.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')