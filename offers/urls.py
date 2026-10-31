from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("manage/", views.dashboard, name="dashboard"),
    path(
        "manage/login/",
        auth_views.LoginView.as_view(
            template_name="offers/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("manage/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("manage/<int:pk>/pin/", views.toggle_pin, name="toggle_pin"),
    path("manage/<int:pk>/delete/", views.delete_offer, name="delete_offer"),
]
