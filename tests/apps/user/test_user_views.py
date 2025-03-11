import pytest
from django.urls import reverse


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
    """ "
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
