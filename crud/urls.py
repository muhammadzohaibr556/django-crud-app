from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(home) , name="home"),
    path('create',login_required(createPost) , name="create"),
    path('detail/<int:id>',login_required(detail) , name="detail"),
    path('delete/<int:id>',login_required(deletePost) , name="delete"),
]