from django.urls import path

from . import views
from blog import views as blog_views

app_name = "login"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_request, name='logout'),
]
