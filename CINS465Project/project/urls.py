from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name="indexPage"),
    path('testPage/', views.testPage, name="testPage"),
]