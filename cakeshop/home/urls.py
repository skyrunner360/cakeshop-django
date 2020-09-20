from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    # The below line redirects to the home app's urls.py file
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    # the below line redirects to the blog app's urls if /blog is appended
]