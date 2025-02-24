from django.urls import path

from authentication import views

urlpatterns = [
    path("sign-in", views.SignInView.as_view(), name="sign-in"),
]
