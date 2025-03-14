from typing import Optional

from django.forms import CharField, Form, ModelForm, ValidationError

from authentication.models import AppUser


class SignInForm(Form):
    """
    Sign in form.

    Attributes
    ----------
    email : CharField
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
    _validate_user_credentials() -> None
        Validates the user credentials.
    """

    email = CharField()
    password = CharField()

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


class SignUpForm(ModelForm):
    """
    Sign up form.
    """

    class Meta:
        """
        Form metadata.

        Attributes
        ----------
        model : AppUser
            The model associated with the form.
        fields : list[Literal["first_name"], Literal["username"], Literal["email"], Literal["password"]]
            The fields to include in the form.
        """

        model = AppUser
        fields = ["first_name", "username", "email", "password"]
