from django.urls import path

from apps.static_pages import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
