#from ast import main
from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import os
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/About.html')

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

class MainCreatePost(LoginRequiredMixin, CreateView):
    model=Post
    fields=['name', 'phone_number', 'cur_to_get', 'cur_to_give', 'amount', 'area', 'city', 'comment']

    def form_valid(self, form):
        #form.instance.user = self.request.user
        obj=form.save(commit=False)
        obj.user = str(self.request.user)
        # need to add verification to fields.
        obj.save()
        return super().form_valid(form)
