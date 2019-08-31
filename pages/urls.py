from django.urls import path, include
from . import views

urlpatterns =[
  path('', views.index, name='index'),
  path('login', include('social_django.urls', namespace='social')),
]