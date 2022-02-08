from django.urls import path
from .views import (PostListView, PostDetailView , PostCreateView, 
                    PostUpdateView, PostDeleteView, UserPostListView)
from . import views #import the view model from the current folder

#the "name" in the "path" uniquely identifies each url for easy reference later in other files (like the templates)
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'), #route for individual posts #pk=blog id 
    path('post/new/', PostCreateView.as_view(), name='post-create'), #creating a new post
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'), #route for individual posts #pk=blog id 
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about,name='blog-about'),
]

