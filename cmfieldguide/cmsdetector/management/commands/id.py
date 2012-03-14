from django.core.management.base import NoArgsCommand
from optparse import make_option
import util

class Command(NoArgsCommand):
    help = "Whatever you want to print here"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
        )

    def handle_noargs(self, **options):
        self.stdout.write(populate_tests)