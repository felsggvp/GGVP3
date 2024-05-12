from django.urls import path
from . import views

urlpatterns = [
    path('kk/', views.helloworld, name="helloworld"),
    path('oguzok/', views.oguzik, name="oguzik"),
    path('', views.oguzik, name="chuhu")
]
