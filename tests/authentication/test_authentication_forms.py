import pytest

from authentication.forms import SignInForm
from tests.conftest import USER_DATA_TEST


def test_sign_in_form_invalid_data():
    """
    GIVEN an invalid email and password,
    WHEN the sign in form is initialized,
    THEN the field errors are returned.
    """

    # Arrange
    data = {"email": "not_an_email", "password": "admin1234"}

    # Act
    form = SignInForm(data)

    # Assert
    assert form.errors.get("email") == ["Enter a valid email address."]
    assert form.errors.get("password") == ["This password is too common."]


@pytest.mark.django_db
def test_sign_in_form_invalid_credentials():
    """
    GIVEN a group of credentials that do not correspond to any user,
    WHEN the sign in form is initialized,
    THEN the invalid credentials error is returned.
    """

    # Arrange
    data = {"email": "valid@email.com", "password": "valid_1234"}

    # Act
    form = SignInForm(data)

    # Assert
    assert form.non_field_errors() == ["Invalid email or password"]


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user")
def test_sign_in_form_invalid_success():
    """
    GIVEN a group of credentials that correspond to an existing user,
    WHEN the sign in form is initialized,
    THEN no error is generated.
    """

    # Arrange
    data = {"email": USER_DATA_TEST["email"], "password": USER_DATA_TEST["password"]}

    # Act
    form = SignInForm(data)

    # Assert
    assert not form.errors
    assert not form.non_field_errors()
