#!/usr/bin/env python
"""Django"s command-line utility for administrative tasks."""
import os
import sys

from django.conf import settings

def main():
    is_testing = "test" in sys.argv

    if is_testing:
        cov = configure_coverage()

    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houseplant_reminder.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    if is_testing:
        teardown_coverage(cov)

def configure_coverage():
    import coverage
    cov = coverage.coverage(source=settings.COVERAGE_INCLUDES, omit=settings.COVERAGE_OMITS)
    cov.set_option("report:show_missing", True)
    cov.erase()
    cov.start()
    return cov

def teardown_coverage(cov):
    cov.stop()
    cov.save()
    cov.html_report(directory="coverage")


if __name__ == "__main__":
    main()