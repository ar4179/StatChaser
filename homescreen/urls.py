from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.graph,name='home-page'),
    # path('',views.aboutMe,name='about-me'),
    path('aboutme',views.aboutMe,name='about-me')
]