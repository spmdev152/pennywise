from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.static_content.urls")),
    path("authentication/", include("authentication.urls")),
    path("user/", include("apps.user.urls")),
]
