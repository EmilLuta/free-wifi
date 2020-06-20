from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path('create_local/', views.CreateLocal.as_view(), name='create_local'),
    path('create_password/', views.CreatePassword.as_view(), name='create_password'),
    path("about/", views.about, name="about"),
    path("verify_local/", views.verify_local, name="verify_local"),
    path("verify_local/<int:pk>", views.verify_this_local, name="verify_this_local"),
]