from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import Post, Replie, Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, EditProfileForm, ProfileForm
from .models import Profile, UpdateProfileForm






def forum(request):
    profile = Profile.objects.all()
    if request.method=="POST":   
        user = request.user
        image = request.user.profile.image
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content, image=image)
        post.save()
        alert = True
        return render(request, "forum.html", {'alert':alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "forum.html", {'posts':posts})

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
        return render(request, "discussion.html", {'alert':alert})
    return render(request, "discussion.html", {'post':post, 'replies':replies})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url = '/login')
def myprofile(request):
    if request.method=="POST":
        user = request.user    
        profile = Profile(user=user)
        profile.save()
        form = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "profile.html",{'obj':obj})
    else:
        form=ProfileForm()
    return render(request, "profile.html", {'form':form})



def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/contact.html")


def privacy(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/privacy.html")

def terms(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "legal/terms.html")

def password_reset(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "registration/password_reset.html")
