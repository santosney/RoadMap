from django.urls import path
from . import views
from rest_framework import routers
urlpatterns = [
 
    
    path('listuser/', views.listuser),
    path('addUser/', views.addUser),
    path('listpublication/', views.lis_publication),
    path('addPublication/', views.addPublication),
    path('UpdateUser/<int:id>/', views.UpdateUser),
    path('UpdatePublication/<int:id>/', views.UpdatePublication),
    path('login/', views.login),
    
]