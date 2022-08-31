from django.urls import path
from olx import views

urlpatterns = [
    path("", views.dashboard, name="home"),
]