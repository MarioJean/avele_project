from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('<slug:slug>-<int:pk>/', views.blogpost, name='blogpost'),
    path('search', views.search, name='search'),
]
