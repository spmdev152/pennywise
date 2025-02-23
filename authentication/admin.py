from django.contrib import admin

from authentication.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    """
    App user model inside the admin.

    Attributes:
        list_display (tuple[Literal["username"], Literal["email"]]): The fields to display inside the admin. Defaults to ("username", "email").
    """

    list_display = ("username", "email")
