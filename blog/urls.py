from django.urls import path,include
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    # path('',views.home,name='blog-home'),
    path('',PostListView.as_view(),name='blog-home'), # looks for -> <app>/<model>_<view_type>.html
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('fav/<int:id>',views.favourite_add,name='favourite_add'),
    path('user/favourites/',views.favourite_list,name='favourite_list'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about'),
]
