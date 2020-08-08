from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('create', views.blogging, name="create"),
    path('show', views.show, name="show"),
    path('update', views.update, name="update"),
    path('delete', views.destroy, name="delete"),
]
