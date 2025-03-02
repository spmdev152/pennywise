from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Authentication app configuration.

    Attributes
    ----------
    default_auto_field : str
        The primary key type of the models of the application.
        By default is "django.db.models.BigAutoField".
    name : str
        The path of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
