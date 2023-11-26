"""drf_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route

from profiles import views as profiles_views
from posts import views as posts_views
from comments import views as comments_views
from likes import views as likes_views
from followers import views as followers_views

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path('profiles/', profiles_views.ProfileList.as_view()),
    path('profiles/<int:pk>/', profiles_views.ProfileDetail.as_view()),
    path('posts/', posts_views.PostList.as_view()),
    path('posts/<int:pk>/', posts_views.PostDetail.as_view()),
    path('comments/', comments_views.CommentList.as_view()),
    path('comments/<int:pk>/', comments_views.CommentDetail.as_view()),
    path('likes/', likes_views.LikeList.as_view()),
    path('likes/<int:pk>/', likes_views.LikeDetail.as_view()),
    path('followers/', followers_views.FollowerList.as_view()),
    path('followers/<int:pk>/', followers_views.FollowerDetail.as_view()),
]