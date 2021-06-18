from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("main/", views.main_view, name="main"),
    path("", views.first_view, name="first"),
]