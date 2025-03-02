import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user_and_login")
def test_sign_in_view_get_method_authenticated_user(http_client):
    """
    GIVEN an authenticated user,
    WHEN a GET request is made to the sign in view,
    THEN the response status code is 302.
    """

    # Act
    response = http_client.get(reverse("sign-in"))

    # Assert
    assert response.status_code == 302

    # TODO assert the rendered template is the expected one


def test_sign_in_view_get_method_success(http_client):
    """
    WHEN a GET request is made to the sign in view,
    THEN the response status code is 200,
    AND the sign in template is rendered.
    """

    # Act
    response = http_client.get(reverse("sign-in"))
    rendered_templates = [template.name for template in response.templates]

    # Assert
    assert response.status_code == 200
    assert "pages/authentication/sign-in.html" in rendered_templates


def test_sign_in_view_post_method_invalid_data(http_client):
    """
    GIVEN an invalid email and password,
    WHEN a POST request is made to the sign in view,
    THEN the response status code is 400.
    """

    # Arrange
    data = {"email": "not_an_email", "password": "admin1234"}

    # Act
    response = http_client.post(reverse("sign-in"), data)

    # Assert
    assert response.status_code == 400


@pytest.mark.django_db
def test_sign_in_view_post_method_invalid_credentials(http_client):
    """
    GIVEN a group of credentials that do not correspond to any user,
    WHEN a POST request is made to the sign in view,
    THEN the response status code is 403.
    """

    # Arrange
    data = {"email": "valid@email.com", "password": "valid_1234"}

    # Act
    response = http_client.post(reverse("sign-in"), data)

    # Assert
    assert response.status_code == 403


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user")
def test_sign_in_view_post_method_success(http_client):
    """
    GIVEN a group of credentials that correspond to an existing user,
    WHEN a POST request is made to the sign in view,
    THEN the response url is /user/account.
    """

    # Arrange
    data = {"email": "test_user@email.com", "password": "test_pwd_1234"}

    # Act
    response = http_client.post(reverse("sign-in"), data)

    # Assert
    assert response.url == "/user/account"

    # TODO remove the existing and assert the rendered template is the expected one
