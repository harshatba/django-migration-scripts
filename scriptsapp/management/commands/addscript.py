import os
import time

from django.core.management.base import BaseCommand, CommandError
from scriptsapp.models import MigrationScripts

template = """from {} import models
"""

class Command(BaseCommand):
    help = 'Adds a script to write after a migration is applied'

    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, app, *args, **options):
        path_to_dir = os.getcwd() + '/' + app

        if not os.path.exists(path_to_dir):
            CommandError('Are you sure app "{}" exists?'.format(app))

        print(os.listdir(path_to_dir + '/migrations/')[-1])
        scripts_dir = path_to_dir + '/scripts/'
        if not os.path.exists(scripts_dir):
            os.makedirs(scripts_dir)
        filenames = os.listdir(scripts_dir)
        numbered_filenames = list(map(lambda fname: int(fname.split('.')[0]), filenames))
        numbered_filenames.sort(reverse=True)
        migration_related_to = numbered_filenames[-1]
        script_name = self.get_script_name()
        f = open(scripts_dir + script_name, 'w+')
        f.write(template.format(app))
        f.close()
        print(scripts_dir + script_name)
        MigrationScripts.objects.create(app=app, name=script_name, migration_name=migration_related_to)

    def get_script_name(self):
        return str(round(time.time())) + '.py'
