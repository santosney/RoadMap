from django.urls import path
from . import views
from rest_framework import routers
urlpatterns = [
 
    
    path('listuser', views.listuser),
    path('addUser', views.addUser),
    path('listpublication', views.lis_publication),
    path('addPublication', views.addPublication),
    path('UpdateUser', views.UpdateUser),
    path('UpdatePublication', views.UpdatePublication),
    path('login', views.login),
    path('delete_user', views.delete_user),
    path('deletePublication', views.deletePublication)
    
]