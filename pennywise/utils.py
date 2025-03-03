import os


def check_environment_variables():
    """
    Checks if the environment variables are set.

    Raises
    ------
    EnvironmentError
        If the ENVIRONMENT environment variable is not set.
    EnvironmentError
        If the SECRET_KEY environment variable is not set.
    """

    if not os.getenv("ENVIRONMENT"):
        raise EnvironmentError("ENVIRONMENT not found")

    if not os.getenv("SECRET_KEY"):
        raise EnvironmentError("SECRET_KEY not found")
