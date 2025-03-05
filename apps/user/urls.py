from django.urls import path

from apps.user import views

urlpatterns = [
    path("account", views.AccountView.as_view(), name="account"),
]
