import pytest
from django.test import Client

from authentication.models import AppUser

USER_DATA_TEST = {
    "username": "test_user",
    "email": "test_user@email.com",
    "password": "test_pwd_1234",
}


@pytest.fixture(name="http_client")
def client_fixture() -> Client:
    """
    Http client fixture.

    Returns
    -------
    Client
        The http client instance.
    """

    return Client()


@pytest.fixture(name="create_user")
def create_user_fixture() -> None:
    """
    Create user fixture.
    """

    AppUser.objects.create_user(**USER_DATA_TEST)


@pytest.fixture(name="create_user_and_login")
def create_user_and_login_fixture(http_client: Client) -> None:
    """
    Create user and login fixture.

    Parameters
    ----------
    http_client : Client
        The http client.
    """

    user = AppUser.objects.create_user(**USER_DATA_TEST)

    http_client.force_login(user)
