from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """Authentication app config.

    Attributes:
        default_auto_field (str): The default type for incrementing primary keys. Defaults to "django.db.models.BigAutoField".
        name (str): The application path. Defaults to "authentication".
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
