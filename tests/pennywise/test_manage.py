import os
from unittest.mock import patch

import pytest

from pennywise.utils import check_environment_variables


@pytest.mark.parametrize(
    "missing_environment_variable, error_message",
    [("ENVIRONMENT", "ENVIRONMENT not found"), ("SECRET_KEY", "SECRET_KEY not found")],
)
def test_check_environment_variables_missing_variable(
    missing_environment_variable, error_message
):
    """
    WHEN check_environment_variables is called with a missing environment variable,
    THEN an EnvironmentError is raised with the correct error message.
    """

    environment_variables = {
        "ENVIRONMENT": "test_environment",
        "SECRET_KEY": "test_secret_key",
    }

    environment_variables.pop(missing_environment_variable)

    with patch.dict(os.environ, environment_variables, clear=True):
        with pytest.raises(EnvironmentError, match=error_message):
            check_environment_variables()
