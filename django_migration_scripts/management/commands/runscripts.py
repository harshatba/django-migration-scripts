import os

from django.apps import apps
from django.core.management.base import BaseCommand

from django_migration_scripts.models import MigrationScripts


class Command(BaseCommand):
    help = 'Adds a script to write after a migration is applied'

    def add_arguments(self, parser):
        parser.add_argument('--app')

    def handle(self, app=None, *args, **options):
        if 'app' in options and not options['app']:
            apps_to_consider = [options['app']]
        else:
            apps_to_consider = apps.app_configs.keys()

        for app in apps_to_consider:
            path_to_dir = os.getcwd() + '/' + app

            if not os.path.exists(path_to_dir):
                continue

            scripts_dir = path_to_dir + '/scripts/'
            if not os.path.exists(scripts_dir):
                os.makedirs(scripts_dir)
            filenames = os.listdir(scripts_dir)
            filenames.sort()
            for filename in filenames:
                if not MigrationScripts.objects.filter(app=app, name=filename).exists():
                    script_path = os.getcwd() + '/' + app + '/scripts/' + filename
                    open(script_path).read()
                    exec(open(script_path).read())
                    print(filename + ' .....DONE')
                    MigrationScripts.objects.create(app=app, name=filename)
