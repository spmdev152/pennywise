from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

APP_USER_NAME_VALIDATOR = RegexValidator(
    regex=r"^[a-zA-Z\s]*$", message="Only letters and spaces are allowed."
)


class AppUser(AbstractUser):
    """App user model.

    Attributes:
        email (models.EmailField): The email address of the user.
        first_name (models.CharField): The first name of the user.
        last_name (models.CharField): The last name of the user.
    """

    email = models.EmailField(
        unique=True, error_messages={"unique": "Email already exists."}
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
        validators=[APP_USER_NAME_VALIDATOR],
    )

    last_name = models.CharField(
        max_length=150,
        blank=True,
        validators=[APP_USER_NAME_VALIDATOR],
    )

    def __str__(self) -> str:
        """String representation of the model.

        Returns:
            str: The email address of the user.
        """

        return self.email

    class Meta:
        """Model metadata.

        Attributes:
            db_table (str): The name of the database table associated with the model. Defaults to "users".
            verbose_name_plural (str): The plural name associated with the model. Defaults to "Users".
        """

        db_table = "users"
        verbose_name_plural = "Users"
