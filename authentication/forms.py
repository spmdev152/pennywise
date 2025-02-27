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
    user : Optional[AppUser]
        The user if the credentials are valid.

    Methods
    -------
    clean() -> None
        Custom form validation.
    _validate_user_credentials(email: str, password: str) -> None
        Validates the user credentials.
    """

    email = EmailField()
    password = CharField(validators=[validate_password])
    user = None

    def clean(self) -> None:
        """
        Custom form validation.
        """

        data = super().clean()

        if not self.errors.get("email") and not self.errors.get("password"):
            self._validate_user_credentials(data["email"], data["password"])

    def _validate_user_credentials(self, email: str, password: str) -> None:
        """
        Validates the user credentials.

        Parameters
        ----------
        email : str
            The email of the user.
        password : str
            The password of the user.

        Raises
        ------
        ValidationError
            If the user credentials are invalid.
        """

        user = AppUser.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            raise ValidationError("Invalid email or password")

        self.user = user
