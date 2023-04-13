import os

from django.conf import settings
from django_scripts.management.commands.cron import CronJobBaseCommand


class Command(CronJobBaseCommand):
    def cron_job(self):
        os.system(f'{settings.BASE_DIR}/venv/bin/isort -rc .')
