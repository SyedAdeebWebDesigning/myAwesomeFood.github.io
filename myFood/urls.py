from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('food', views.food, name='food'),
    path('account', views.account, name='account'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('thanks', views.thanks, name='thanks'),
]


