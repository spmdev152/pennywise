from pennywise.utils import parse_query_string_from_body


def test_parse_query_string_from_body_success():
    """
    GIVEN a valid request body,
    WHEN the body is parsed,
    THEN the query string values are returned.
    """

    # Arrange
    body = b"key1=value1&key2=value2"

    # Act
    result = parse_query_string_from_body(body)

    # Assert
    assert result == {"key1": "value1", "key2": "value2"}
