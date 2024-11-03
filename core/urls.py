
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login/', views.login_page),
    path('profile', views.profile),


    path('save-user', views.save_user),
    path('login-user', views.login_user),
    path('logout-user', views.logout),
    path('profile-user', views.profile),
    path('logout-page', views.logout_page, name="logout-page"),
]