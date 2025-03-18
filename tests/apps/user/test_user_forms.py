import pytest

from apps.user.forms import UserDetailsForm
from tests.constants import TEST_USER_DATA


def test_user_details_form_invalid_data():
    """
    GIVEN a group of invalid values for the user details form,
    WHEN the user details form is initialized,
    THEN the errors are returned.
    """

    # Arrange
    data = {
        "first_name": "first_name_123",
        "username": "",
    }

    # Act
    form = UserDetailsForm(data)

    # Assert
    assert form.errors.get("first_name") == ["Only letters and spaces are allowed."]
    assert form.errors.get("username") == ["This field is required."]


@pytest.mark.django_db
def test_user_details_form_success():
    """
    GIVEN a group of valid values for the user details form,
    WHEN the user details form is initialized,
    THEN no error is generated.
    """

    # Arrange
    data = {
        "first_name": TEST_USER_DATA["first_name"],
        "username": TEST_USER_DATA["username"],
    }

    # Act
    form = UserDetailsForm(data)

    # Assert
    assert not form.errors
    assert not form.non_field_errors()
