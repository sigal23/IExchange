#from ast import main
from pickle import GET
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import os


context = {'posts': Post.objects.all(), 'filters': []}

# Create your views here.
def home(request):
    global context
    if request.method == 'POST':
        currencyGive = request.POST.get('currencyGive')
        areaPost = request.POST.get('area')
        currencyGet = request.POST.get('currencyGet')
        toAmount = request.POST.get('toAmount')
        fromAmount = request.POST.get('fromAmount')
        filters = Post.objects.filter(area=areaPost)
        context['filters'] = filters
        return HttpResponseRedirect('/')
    return render(request, 'main/home.html', context)

# posts=[]
# flag=0

# # Create your views here.
# def home(request):
#     global flag
#     global posts
#     if request.method == 'POST':
#         currencyGive = request.POST.get('currencyGive')
#         areaPost = request.POST.get('area')
#         currencyGet = request.POST.get('currencyGet')
#         toAmount = request.POST.get('toAmount')
#         fromAmount = request.POST.get('fromAmount')
#         posts = Post.objects.filter(area=areaPost)
#         flag=1
#         print('##### filter posts ##### ' + str(posts))
#         return HttpResponseRedirect('/')
#     else:
#         print(request)
#         if flag==1:
#             context = {'posts': posts}
#             flag=0
#             print('##### filter context get ##### ' + str(context))
#             return render(request, 'main/home.html', context)
#         else:
#             posts = Post.objects.all()
#             context = {'posts': []}
#             print('$$$ all posts $$$ ' + str(posts))
#             print('$$$ all posts $$$ ' + str(flag))
#             return render(request, 'main/home.html', context)

def personal_post(request):
    posts = Post.objects.filter(user=str(request.user))
    context = {'posts': posts}
    return render(request, 'main/personal_post.html', context)


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

class MainUpdatePost(LoginRequiredMixin, UpdateView):
    model=Post
    fields=['name', 'phone_number', 'cur_to_get', 'cur_to_give', 'amount', 'area', 'city', 'comment']

    def get_object(self):
        post = super(MainUpdatePost, self).get_object()
        #if not todo.user == self.request.user:
        #    raise Http404('You dontt have permission to do this. go away you hacker')
        return post