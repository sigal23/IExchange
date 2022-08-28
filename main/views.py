from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
import os
# Create your views here.
def home(request):
    print("i am here")
    posts = Post.objects.all()
    context = {'posts': posts}
    print("i am here2")
    return render(request, 'main/home.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'main/post_list.html', context)

def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html',
                      {'form': UserCreationForm()})
    else:
        form = UserCreationForm(request.POST)
        print("post")
        if form.is_valid():
            print("is valid")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticate(username=username, password=raw_password)
            user = get_user_model().objects.get(username=username)
            print("user created")
            login(request, user)
            print("logged in")
            return home(request)
        else:
            print("not valid")
            error = form.errors
            return render(request, 'registration/signup.html', {'form':UserCreationForm(), 'error': error})