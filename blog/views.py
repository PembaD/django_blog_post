#'The view deals with presentation of data and database to the client in a nice format'
# this is the blog-view
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from .models import Post 
from django.contrib.auth.models import User

#function view 
#no longer used since class-based views are being used
def home(request):
    #create a dict
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context) 

#'ListView' is a type of class-based view
# ***HOME Page***
class PostListView(ListView): 
    model = Post 
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #the html template loops through 'posts'
    ordering = ['-date_posted'] #order the posts from newest to oldest
    paginate_by = 5 #list only 2 posts per page

#sticking to the View conventions can reduce the number of lines of code
#'DetailView' for individual posts
class PostDetailView(DetailView):
    #the template naming convention is '<app>/<model>_<viewtype>.html e.g. blog/post_detail.html 
    model = Post

#allows user to create a new 'post'
#'LoginRequiredMixin' requires a user to be logged in before creating a new post
class PostCreateView(LoginRequiredMixin, CreateView): #if not logged in, redirect to log in page
    #the naming convention for creat template is '<app>/<model>_form.html' e.g. blog/post_form.html
    model = Post
    fields = ['title', 'content']

    #before submitting the form, set the author to current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#allows user to update their 'post'
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #if not logged in, redirect to log in page
    #the naming convention for update template is '<app>/<model>_form.html' e.g. blog/post_form.html
    model = Post
    fields = ['title', 'content']

    #before submitting the form, set the author to current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #only users who created the post can update the post
    def test_func(self):
        post = self.get_object() #gets the Post currently trying to update
        if self.request.user == post.author: 
            return True
        return False

#deleting a post
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    #the template naming convention is '<app>/<model>_confirm_delete.html
    #only users who created the post can delete the post
    def test_func(self):
        post = self.get_object() #gets the Post currently trying to update
        if self.request.user == post.author: 
            return True
        return False

    #redirect after the post is deleted
    success_url = '/' #redirects to the home page

#display only posts from an individual user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    #override queryset of the base class
    #a query is a request for data or information from a database table or combination of tables
    def get_queryset(self):
        #check if a user(specified in the url) exists in the database
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def about(request):
    return render(request,'blog/about.html',{'title':'About'})


