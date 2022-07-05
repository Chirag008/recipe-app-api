"""
Django command to wait for database to be available
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to Wait for Database."""

    def handle(self, *args, **options):
        pass