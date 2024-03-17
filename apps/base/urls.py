from django.urls import path

from apps.base import views as base

urlpatterns = [
    path('', base.index, name="index")
    
]   