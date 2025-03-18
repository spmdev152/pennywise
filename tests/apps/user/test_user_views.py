import pytest
from django.urls import reverse

from tests.constants import TEST_USER_DATA


def test_account_view_get_method_unauthenticated_user(http_client):
    """
    GIVEN an unauthenticated user,
    WHEN a GET request is made to the account view,
    THEN the response status code is 302,
    AND the response url is /user/sign-in?next=/user/account.
    """

    # Act
    response = http_client.get(reverse("account"))

    # Assert
    assert response.status_code == 302
    assert response.url == f"{reverse('sign-in')}?next={reverse('account')}"


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user_and_login")
def test_account_view_get_method_success(http_client):
    """
    GIVEN an authenticated user,
    WHEN a GET request is made to the account view,
    THEN the response status code is 200,
    AND the account template is rendered.
    """

    # Act
    response = http_client.get(reverse("account"))
    rendered_templates = [template.name for template in response.templates]

    # Assert
    assert response.status_code == 200
    assert "pages/user/account.html" in rendered_templates


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user_and_login")
def test_account_view_patch_method_invalid_data(http_client):
    """
    GIVEN a group of invalid values for the update user details process,
    WHEN a PATCH request is made to the account view,
    THEN the response contains the errors.
    """

    # Arrange
    body = "first_name=first_name_123"

    # Act
    response = http_client.patch(
        reverse("account"),
        data=body,
        content_type="application/x-www-form-urlencoded",
    )

    # Assert
    assert '<p class="field-error" id="first_name-error"' in response.content.decode()
    assert '<p class="field-error" id="username-error"' in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user_and_login")
def test_account_view_patch_method_success(http_client):
    """
    GIVEN a group of valid values for the update user details process,
    WHEN a PATCH request is made to the account view,
    THEN the response contains a toast message.
    """

    # Arrange
    body = f"first_name={TEST_USER_DATA['first_name']}&username={TEST_USER_DATA['username']}"

    # Act
    response = http_client.patch(
        reverse("account"),
        data=body,
        content_type="application/x-www-form-urlencoded",
    )

    # Assert
    assert 'id="user-details-toast"' in response.content.decode()
