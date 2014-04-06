from django.core.management.base import BaseCommand
from django.conf import settings

import logging


logger = logging.getLogger('retrieve_tweets')
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):
    args = ''
    help = 'no arguments required'

    def handle(self, *args, **options):
        #users = User.objects.all()
        pass