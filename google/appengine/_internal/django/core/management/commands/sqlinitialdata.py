from __future__ import absolute_import
from google.appengine._internal.django.core.management.base import AppCommand, CommandError

class Command(AppCommand):
    help = "RENAMED: see 'sqlcustom'"

    def handle(self, *apps, **options):
        raise CommandError("This command has been renamed. Use the 'sqlcustom' command instead.")
