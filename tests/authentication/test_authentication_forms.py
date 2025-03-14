import pytest

from authentication.forms import SignInForm, SignUpForm
from tests.constants import TEST_USER_DATA


def test_sign_in_form_invalid_data():
    """
    GIVEN a group of invalid values for the sign in form,
    WHEN the sign in form is initialized,
    THEN the errors are returned.
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


def test_sign_up_form_invalid_data():
    """
    GIVEN a group of invalid values for the sign up form,
    WHEN the sign up form is initialized,
    THEN the errors are returned.
    """

    # Arrange
    data = {
        "first_name": "first_name_123",
        "username": "",
        "email": "not_an_email",
        "password": "admin1234",
    }

    # Act
    form = SignUpForm(data)

    # Assert
    assert form.errors.get("first_name") == ["Only letters and spaces are allowed."]
    assert form.errors.get("username") == ["This field is required."]
    assert form.errors.get("email") == ["Enter a valid email address."]
    assert form.errors.get("password") == ["This password is too common."]


@pytest.mark.django_db
def test_sign_up_form_success():
    """
    GIVEN a group of valid values for the sign up form,
    WHEN the sign up form is initialized,
    THEN no error is generated.
    """

    # Arrange
    data = {
        "first_name": TEST_USER_DATA["first_name"],
        "username": TEST_USER_DATA["username"],
        "email": TEST_USER_DATA["email"],
        "password": TEST_USER_DATA["password"],
    }

    # Act
    form = SignUpForm(data)

    # Assert
    assert not form.errors
    assert not form.non_field_errors()
