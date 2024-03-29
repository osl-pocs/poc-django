#!/usr/bin/env python
import os
import sys
from pathlib import Path

import environ

if __name__ == "__main__":
    ROOT_DIR = Path(__file__).resolve(strict=True).parent
    env = environ.Env()
    env.read_env(str(ROOT_DIR / ".env"))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # poc_django directory.
    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "poc_django"))

    # Override default port for `runserver` command
    from django.core.management.commands.runserver import Command as runserver

    runserver.default_port = "8081"

    execute_from_command_line(sys.argv)
