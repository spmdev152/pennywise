from django.urls import reverse


def test_home_view_get_method_success(http_client):
    """
    WHEN a GET request is made to the home view,
    THEN the response status code is 200,
    AND the home template is rendered.
    """

    # Act
    response = http_client.get(reverse("home"))
    rendered_templates = [template.name for template in response.templates]

    # Assert
    assert response.status_code == 200
    assert "pages/static_content/home.html" in rendered_templates
