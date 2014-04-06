from django.core.management.base import BaseCommand
from django.conf import settings

import logging
from core.models import Area, SourceForArea


logger = logging.getLogger('retrieve_tweets')
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):
    args = ''
    help = 'no arguments required'

    def handle(self, *args, **options):
        s_list = SourceForArea.objects.all()
        for s in s_list:
            s.fetch_twitter_entries()