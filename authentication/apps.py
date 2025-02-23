from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Authentication app configuration.

    Attributes
    ----------
    default_auto_field : str
        The increment type used in the primary keys of the models of the app. By default is "django.db.models.BigAutoField".
    name : str
        The application path. By default is "authentication".
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
