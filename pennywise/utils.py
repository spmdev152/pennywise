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


def parse_query_string_from_body(body: bytes) -> dict[str, str]:
    """
    Parses a query string from a request body.

    Parameters
    ----------
    body : bytes
        The body of a request.

    Returns
    -------
    dict[str, str]
        The query string values.
    """

    body_string = body.decode("utf-8")

    query_string_values = {}

    if not body_string:
        return query_string_values

    query_string_pairs = body_string.split("&")

    for pair in query_string_pairs:
        key, value = pair.split("=")
        query_string_values[key] = value

    return query_string_values
