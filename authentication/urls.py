from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('service', views.service, name="service"),
    path('ac', views.ac, name = "ac"),
    path('tv', views.tv, name = "tv"),
    path('renovator', views.renovators, name = "renovator"),
    path('plumbers', views.plumbers, name = "plumbers"),
    path('electrician', views.electricians, name = "electrician"),
    path('carpenter', views.carpenters, name = "carpenter"),
    path('housekeeper', views.housekeeper, name = "housekeeper"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('aboutpage',views.about_page, name='aboutpage')

]


    
