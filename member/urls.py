from django.contrib import admin
from django.urls import path,include
from .views import userCreationView

urlpatterns = [
    path('signup/', userCreationView.as_view(), name='signup'),    
]