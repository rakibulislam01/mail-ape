from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('Logout', LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
]
