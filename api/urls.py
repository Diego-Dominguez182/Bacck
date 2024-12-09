from django.urls import path
from . import views

urlpatterns = [
    path('builds', views.getBuilds),
    path('builds/createBuild', views.createBuild),
    path('builds/<str:name>/', views.getBuildByName),
    path('builds/delete/<int:idSearch>/', views.deletByID),
    path('login/', views.login),
    path('register/', views.register, name='register'),
]