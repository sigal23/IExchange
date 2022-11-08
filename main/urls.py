from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create_post', views.MainCreatePost.as_view(), name='create_post'),
    path('about', views.about, name='about'),
    path('personal_post', views.personal_post, name='personal_post'),
    path('update_post/<int:pk>', views.MainUpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', views.MainDeletePost.as_view(), name='delete_post'),
    
]
