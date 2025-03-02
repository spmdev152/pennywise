from typing import Optional

from django.contrib.auth.password_validation import validate_password
from django.forms import CharField, EmailField, Form, ValidationError

from authentication.models import AppUser


class SignInForm(Form):
    """
    Sign in form.

    Attributes
    ----------
    email : EmailField
        The email field.
    password : CharField
        The password field.

    Properties
    ----------
    user() -> Optional[AppUser]
        Retrieves the user associated with the email in the form.

    Methods
    -------
    clean() -> None
        Custom form validation.
    _validate_user_credentials(email: str, password: str) -> None
        Validates the user credentials.
    """

    email = EmailField()
    password = CharField(validators=[validate_password])

    @property
    def user(self) -> Optional[AppUser]:
        """
        Retrieves the user associated with the email in the form.

        Returns
        -------
        Optional[AppUser]
            The user if found, otherwise None.
        """

        return AppUser.objects.filter(email=self.data["email"]).first()

    def clean(self) -> None:
        """
        Custom form validation.
        """

        super().clean()

        if not self.errors.get("email") and not self.errors.get("password"):
            self._validate_user_credentials()

    def _validate_user_credentials(self) -> None:
        """
        Validates the user credentials.

        Raises
        ------
        ValidationError
            If the email or password is incorrect.
        """

        if not self.user or not self.user.check_password(self.data["password"]):
            raise ValidationError("Invalid email or password")
