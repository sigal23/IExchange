from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create_post', views.MainCreatePost.as_view(), name='create_post'),
    path('', views.home, name='home'),
]
