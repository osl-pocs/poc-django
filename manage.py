#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from pathlib import Path
import sys

from dotenv import load_dotenv

env_path = os.path.join(
    Path(__file__).resolve().parent,
    '.env'
)
load_dotenv(env_path)

DJANGO_ENV_NAME = os.getenv('DJANGO_ENV_NAME')

def main():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', f'config.settings.{DJANGO_ENV_NAME}'
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
