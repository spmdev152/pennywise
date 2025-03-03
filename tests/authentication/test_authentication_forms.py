import pytest

from authentication.forms import SignInForm
from tests.constants import TEST_USER_DATA


def test_sign_in_form_invalid_data():
    """
    GIVEN an empty email and password,
    WHEN the sign in form is initialized,
    THEN the email and password errors are returned.
    """

    # Arrange
    data = {"email": "", "password": ""}

    # Act
    form = SignInForm(data)

    # Assert
    assert form.errors.get("email") == ["This field is required."]
    assert form.errors.get("password") == ["This field is required."]


@pytest.mark.django_db
def test_sign_in_form_invalid_credentials():
    """
    GIVEN a group of credentials that do not correspond to any user,
    WHEN the sign in form is initialized,
    THEN the invalid credentials error is returned.
    """

    # Arrange
    data = {"email": "incorrect_email", "password": "incorrect_password"}

    # Act
    form = SignInForm(data)

    # Assert
    assert form.non_field_errors() == ["Invalid email or password"]


@pytest.mark.usefixtures("create_user")
@pytest.mark.django_db
def test_sign_in_form_success():
    """
    GIVEN a group of credentials that correspond to an existing user,
    WHEN the sign in form is initialized,
    THEN no error is generated.
    """

    # Arrange
    data = {"email": TEST_USER_DATA["email"], "password": TEST_USER_DATA["password"]}

    # Act
    form = SignInForm(data)

    # Assert
    assert not form.errors
    assert not form.non_field_errors()
