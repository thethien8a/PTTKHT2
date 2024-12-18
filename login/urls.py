from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login.html/', views.LoginView, name='login'),
    path('register.html/',views.RegisterView, name = 'register'),
    path('why.html/',views.WhyPage,name='why'),
    path('about.html/',views.AboutPage,name="about"),
    path('team.html/',views.TeamPage,name="team"),
    path('service.html/',views.ServicePage,name="service"),
]