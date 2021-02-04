from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail')
]
