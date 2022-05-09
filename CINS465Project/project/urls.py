from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('testPage/', views.testPage, name="testPage"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('profilePage/', views.profilePage, name="profilePage"),
    path('mainFeed/', views.mainFeed, name="mainFeed"),
    path('Error404/', views.Error404, name="Error404"),
]