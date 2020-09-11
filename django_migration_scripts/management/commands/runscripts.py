import os

from django_migration_scripts import MigrationScripts

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Adds a script to write after a migration is applied'

    def add_arguments(self, parser):
        parser.add_argument('--app')

    def handle(self, app=None, *args, **options):
        if 'app' in options and not options['app']:
            queryset = MigrationScripts.objects.filter(applied=False, app=options['app']).order_by('id')
        else:
            queryset = MigrationScripts.objects.filter(applied=False).order_by('id')

        for migration_script in queryset:
            script_path = os.getcwd() + '/' + migration_script.app + '/scripts/' + migration_script.name
            print(script_path)
            open(script_path).read()
            exec(open(script_path).read())
            print(migration_script.name + ' .....DONE')
