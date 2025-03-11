import pytest
from django.urls import reverse

from tests.constants import TEST_USER_DATA


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user_and_login")
def test_sign_in_view_get_method_authenticated_user(http_client):
    """
    GIVEN an authenticated user,
    WHEN a GET request is made to the sign in view,
    THEN the response status code is 302,
    AND the response url is /user/account.
    """

    # Act
    response = http_client.get(reverse("sign-in"))

    # Assert
    assert response.status_code == 302
    assert response.url == reverse("account")


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


def test_sign_in_view_get_method_next_parameter(http_client):
    """
    WHEN a GET request is made to the sign in view with a next parameter,
    THEN the response status code is 200,
    AND the redirection_value is in the response context.
    """

    # Act
    response = http_client.get(f"{reverse('sign-in')}?next={reverse('account')}")

    # Assert
    assert response.status_code == 200
    assert "redirection_message" in response.context


def test_sign_in_view_post_method_invalid_data(http_client):
    """
    GIVEN an empty email and password,
    WHEN a POST request is made to the sign in view,
    THEN the response contains the email and password errors.
    """

    # Arrange
    data = {"email": "", "password": ""}

    # Act
    response = http_client.post(reverse("sign-in"), data)

    # Assert
    assert '<p class="field-error" id="email-error"' in response.content.decode()
    assert '<p class="field-error" id="password-error"' in response.content.decode()


@pytest.mark.django_db
def test_sign_in_view_post_method_invalid_credentials(http_client):
    """
    GIVEN a group of credentials that do not correspond to any user,
    WHEN a POST request is made to the sign in view,
    THEN the response contains the credentials error.
    """

    # Arrange
    data = {"email": "email", "password": "password"}

    # Act
    response = http_client.post(reverse("sign-in"), data)

    # Assert
    assert '<p class="form-error" id="credentials-error"' in response.content.decode()


@pytest.mark.usefixtures("create_user")
@pytest.mark.django_db
def test_sign_in_view_post_method_success(http_client):
    """
    GIVEN a group of credentials that correspond to an existing user,
    WHEN a POST request is made to the sign in view,
    THEN the response url is /user/account.
    """

    # Arrange
    data = {"email": TEST_USER_DATA["email"], "password": TEST_USER_DATA["password"]}

    # Act
    response = http_client.post(reverse("sign-in"), data)

    # Assert
    assert response.url == reverse("account")


@pytest.mark.django_db
@pytest.mark.usefixtures("create_user_and_login")
def test_sign_out_view_post_method_success(http_client):
    """
    GIVEN an authenticated user,
    WHEN a POST request is made to the sign out view,
    THEN the response status code is 200,
    AND the response url is /user/sign-in.
    """

    # Act
    response = http_client.post(reverse("sign-out"))

    # Assert
    assert response.status_code == 200
    assert response.url == reverse("sign-in")
