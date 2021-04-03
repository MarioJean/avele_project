from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('blogpost<int:blogpost_id>', views.blogpost, name='blogpost'),
    path('search', views.search, name='search'),
]
