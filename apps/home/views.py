
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "home/index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def login(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "accounts/login.html")


def register(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "accounts/register.html")


def logout(request):
    # return HttpResponse('Hello from Python!')
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, "index.html")

def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/contact.html")


def privacy(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/privacy.html")

def terms(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/terms.html")

def services(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "home/services.html")

