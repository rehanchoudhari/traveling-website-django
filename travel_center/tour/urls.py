from django.urls import path, include
from .import views
 

urlpatterns = [
    path('',views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('detail', views.detail, name='detail'),
    path('checking/<int:id>', views.checking, name='checking'),
   
]