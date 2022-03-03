from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    path('preview1/', views.preview1),
    path('preview2/', views.preview2),
    path('preview3/', views.preview3),
    path('preview4/', views.preview4),
]