from django.contrib import admin
from django.urls import path,include 
from .import views 

urlpatterns = [
    path('',views.blogHome,name='blog'),
    path('postComment',views.postComment,name='poatComment'),
    # api to post a comment 
    path('<str:slug>/',views.blogPost,name='blog'),
]