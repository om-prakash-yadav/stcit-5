from django.urls import path
from . import views

app_name='cit2020'
urlpatterns = [
    path('', views.index, name='index'),
    path('answer/', views.answer , name='answer'),
    path('lboard/<int:slot>', views.lboard , name='lboard'),
    path('lboard/', views.lboard , name='lboard'),
    path('rules/', views.rules , name='rules'),
    path('about/', views.about, name='about'),
    path('navPage/', views.navPage, name='navPage'),
    path('forms/', views.forms , name='forms'),
    path('quiz/', views.quiz , name='quiz'),
    path('profile/', views.view_profile , name='view_profile'),
    path('profile/update', views.update_profile , name='update_profile'),
    path('qualify/<int:cutoff>', views.qualify , name='qualify'),
]
