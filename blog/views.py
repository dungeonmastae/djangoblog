from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.

# posts = [
#     {
#         'author':'arpit',
#         'title':'Blog Post 1',
#         'content':'First Post Content',
#         'date_posted':'January 11'
#     },
#     {
#         'author':'harshit',
#         'title':'Blog Post 2',
#         'content':'Second Post Content',
#         'date_posted':'January 11'
#     }
#
# ]

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name= 'blog/home.html' # <app>/<model>_<view_type>.html
    context_object_name = 'posts' # because previously the context object was called posts so we could change it to post again which is now set to list
    ordering = ['-date_posted']
    paginate_by=5

class UserPostListView(ListView):
    model = Post
    template_name= 'blog/user_posts.html' # <app>/<model>_<view_type>.html
    context_object_name = 'posts' # because previously the context object was called posts so we could change it to post again which is now set to list
    paginate_by=5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
