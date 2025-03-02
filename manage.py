import os
import sys


def main():
    """
    Launches the server.

    Raises
    ------
    ImportError
        If Django is not available in the environment.
    """

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pennywise.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Django not found")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
