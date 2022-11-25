#from ast import main
from pickle import GET
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.urls import reverse_lazy
from datetime import date
import datetime

context = {'posts': Post.objects.all().order_by('-created_date').values(), 'filters': []}
filters=[]
flag=0


def home(request):
    global flag
    global filters
    global context
    if request.method == 'POST':
        currencyTypes = ['אירו','אפגני אפגני','אריארי מלגשי','בהט תאילנדי','בוליביאנו','בוליבר ונצואלי','ביר אתיופי','בלבואה פנמי','גוורני פראגוואי','גורד האיטי','גילדר של האנטילים ההולנדיים','גריבנה אוקראיני','דולר אוסטרלי','דולר איי שלמה','דולר אמריקאי','דולר בהאמי','דולר בליזי','דולר ברבדיאני','דולר ברוניי','דולר ברמודה','דולר ג׳מייקני','דולר גיאני','דולר הונג קונגי','דולר טייוואני חדש','דולר טרינידדי','דולר ליברי','דולר מזרח קריבי','דולר ניו זילנדי','דולר נמיבי','דולר סורינאמי','דולר סינגפורי','דולר פיג׳י','דולר קיימאני','דולר קנדי','דונג וייטנאמי','דינר אלג׳ירי','דינר בחרייני','דינר טוניסאי','דינר ירדני','דינר כוויתי','דינר לובי','דינר מקדוני','דינר סרבי','דינר עיראקי','דירהם מרוקאי','דירהם של איחוד הנסיכויות הערביות','דלאסי גמבי','דראם ארמני','ואטו של ונואטו','וון דרום קוריאני','וון צפון קוריאני','זלוטי פולני','טאלה סמואי','טאקה בנגלדשי','טוגרוג מונגולי','טנגה קזחסטני','יואן סיני','ין יפני','כתר איסלנדי','כתר דני','כתר נורווגי','כתר שוודי','לאו רומני','לב בולגרי','לוטי לסותי','ליאו מולדובני','ליאון סיירה לאוני','לילנגני סווזי','לירה דרום-סודנית','לירה טורקית חדשה','לירה לבנונית','לירה מצרית','לירה סודנית','לירה סורית','לירה שטרלינג','לירה של איי פוקלנד','למפירה הונדורי','לק אלבני','לרי גאורגי','מאוריטניה אוגיאיה','מאנאט אזרביג׳ני','מאנאט טורקמני','מארק בר המרה של בוסניה־הרצגובינה','מטיקל מוזמביני','נאירה ניגרי','נאקפה אריתראי','נגולטרום בהוטני','סאו טומה ופרינסיפה דברה','סדי גאני','סול פרואני','סום אוזבקי','סום קירגיזי','סומוני טג׳קיסטני','פאונד גיברלטר','פאונד סנט הלני','פאנגה טונגי','פולה בוצוואני','פורינט הונגרי','פזו דומיניקני','פזו מקסיקני','פזו פיליפיני','פזו קובני','פטקה של מקאו','פלורין של ארובה','פסו אורוגוואי','פסו ארגנטינאי','פסו צ׳ילאני','פסו קולומביאני','פרנק בורונדי','פרנק ג׳יבוטי','פרנק גינאי','פרנק פולינזיה הצרפתית','פרנק קומורואי','פרנק קונגולזי','פרנק רואנדי','פרנק שוויצרי','קואנזה אנגולי','קואצ׳ה מלאוי','קוואצ׳ה זמבית','קולון סלבדורי','קולון קוסטה־ריקני','קונה קרואטי','קורדובה ניקרגואה','קורונה צ׳כית','קיאט מיאנמרי','קינה של פפואה גינאה החדשה','קיפ לאי','קצל גואטמלי','ראנד דרום אפריקאי','רובל בלרוסי','רובל רוסי','רופי הודי','רופי מאוריציני','רופי נפאלי','רופי סיישלי','רופי סרי לנקי','רופי פקיסטני','רופיה אינדונזית','רופיה מלדיבית','ריאל איראני','ריאל ברזילאי','ריאל סעודי','ריאל עומאני','ריאל קטארי','ריאל תימני','ריל קמבודי','רינגיט מלזי','שילינג אוגנדי','שילינג טנזני','שילינג סומאלי','שילינג קנייאתי','שקל חדש']
        currencyGive = [request.POST.get('currencyGive')]
        if currencyGive == [None]:
            print("cur give none")
            currencyGive = currencyTypes
        areaPost = [request.POST.get('area')]
        if areaPost == [None]:
            areaPost = ['צפון','דרום','ירושלים והסביבה','מרכז']
        currencyGet = [request.POST.get('currencyGet')]
        if currencyGet == [None]:
            print("cur get none")
            currencyGet = currencyTypes
        toAmount = request.POST.get('toAmount')
        if toAmount == '':
            toAmount=1000000
        print(toAmount)
        fromAmount = request.POST.get('fromAmount')
        if fromAmount == '':
            fromAmount=1
        filters = Post.objects.filter(area__in=areaPost, cur_to_give__in=currencyGet,
        cur_to_get__in=currencyGive,amount__lte=toAmount, amount__gte=fromAmount).order_by('-created_date').values()
        print("^^  POST: ^^" + str(filters))
        if not filters:
            filters = [""]
        flag=1
    else:
        print(flag)
        if flag==1:
            print("##  SHOW FILTER: ##" + str(filters))
            context['filters'] = filters
            flag=0
        else:
            context['filters'] = []
            filters=[]
            print("&&  SHOW ALL: &&" + str(filters))
    return render(request, 'main/home.html', context)


def personal_post(request):
    posts = Post.objects.filter(user=str(request.user))
    context = {'posts': posts}
    return render(request, 'main/personal_post.html', context)


def about(request):
    return render(request, 'main/about.html')

def manual(request):
    return render(request, 'main/manual.html')

def precaution(request):
    return render(request, 'main/precaution.html')

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
        obj=form.save(commit=False)
        obj.user = str(self.request.user)
        today = date.today()
        obj.created_date = today
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

class MainDeletePost(LoginRequiredMixin, DeleteView):
    model=Post
    success_url = reverse_lazy('personal_post')

    def get_object(self):
        post = super(MainDeletePost, self).get_object()
        #if not todo.user == self.request.user:
        #    raise Http404('You dontt have permission to do this. go away you hacker')
        return post