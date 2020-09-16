import os
import time

from django.core.management.base import BaseCommand, CommandError

template = """from {} import models
"""


def get_script_name():
    return str(round(time.time())) + '.py'


class Command(BaseCommand):
    help = 'Adds a script to write after a migration is applied'

    def add_arguments(self, parser):
        parser.add_argument('app')

    def handle(self, app, *args, **options):
        path_to_dir = os.getcwd() + '/' + app

        if not os.path.exists(path_to_dir):
            CommandError('Are you sure app "{}" exists?'.format(app))

        scripts_dir = path_to_dir + '/scripts/'
        if not os.path.exists(scripts_dir):
            os.makedirs(scripts_dir)
        script_name = get_script_name()
        f = open(scripts_dir + script_name, 'w+')
        f.write(template.format(app))
        f.close()
        print(scripts_dir + script_name)
