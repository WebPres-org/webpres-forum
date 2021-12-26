
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def forum(request):
    profile = Profile.objects.all()
    if request.method=="POST":
        user = request.user
        image = request.user.profile.image
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content, image=image)
        post.save()
        alert = True
        return render(request, "forums/forum.html", {'alert':alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "forums/forum.html", {'posts':posts})

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

def forum(request):
    profile = Profile.objects.all()
    if request.method=="POST":
        user = request.user
        image = request.user.profile.image
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content, image=image)
        post.save()
        alert = True
        return render(request, "forums/forum.html", {'alert':alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "forums/forum.html", {'posts':posts})

def discussion(request, myid):
    post = Post.objects.filter(id=myid).first()
    replies = Replie.objects.filter(post=post)
    if request.method=="POST":
        user = request.user
        image = request.user.profile.image
        desc = request.POST.get('desc','')
        post_id =request.POST.get('post_id','')
        reply = Replie(user = user, reply_content = desc, post=post, image=image)
        reply.save()
        alert = True
        return render(request, "forums/discussion.html", {'alert':alert})
    return render(request, "forums/discussion.html", {'post':post, 'replies':replies})