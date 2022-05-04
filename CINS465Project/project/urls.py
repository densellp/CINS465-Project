from django.urls import path
from . import views

urlpatterns = [
    path('testPage/', views.testPage, name="testPage"),
]