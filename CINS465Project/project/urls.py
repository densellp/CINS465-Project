from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('testPage/', views.testPage, name="testPage"),
    path('register/', views.registerUser, name="register"),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('profilePage/', views.profilePage, name="profilePage"),
    path('mainFeed/', views.mainFeed, name="mainFeed"),
    path('Error404/', views.Error404, name="Error404"),
    path('createPost/', views.createPost, name="createPost"),
    path('addLike/<uuid:pk>/', views.addLike, name="addLike"),
    path('logout/', views.logoutUser, name="logout"),
    path('comment/<uuid:pk>/', views.createComment, name="createComment"),
]

# Dedicated to Justin Peters, Rest in Peace 2000-2022