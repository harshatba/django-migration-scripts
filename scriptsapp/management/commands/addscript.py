from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Adds a script to write after a migration is applied'

    def handle(self, *args, **options):
        print(args)
        self.stdout.write(self.style.SUCCESS('Yayyy "%s"' % args))
