from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.graph,name='home-page'),
    path('aboutme',views.aboutMe,name='about-me')
]