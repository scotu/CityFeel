from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.timezone import now

import logging
import requests
from datetime import timedelta
from core.models import Area, SourceForArea, EntryQueue, EntryClassification, ApiRequests


logger = logging.getLogger('retrieve_tweets')
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):
    args = ''
    help = 'no arguments required'

    def handle(self, *args, **options):
        e_list = EntryQueue.objects.filter(analysis=False)[:500]
        for e in e_list:
            params = {'text': e.message}
            if 'mashape' == 'mashape':
                headers = settings.MASHAPE

                ar = ApiRequests.objects.get(name='mashape')
                if ar.counter == 0 and (not ar.until or ar.until < now()):
                    ar.counter = 45000
                    ar.until = now() + timedelta(days=31)
                    ar.save()

                if ar.counter > 0:
                    resp = requests.post('https://japerk-text-processing.p.mashape.com/sentiment/', data=params, headers=headers)
                    print e.message
                    ar.counter -= 1
                    ar.save()
                else:
                    print "no api calls available"
                    return

            # else:
            #     ar = ApiRequests.objects.get(name='textprocessing')
            #     resp = requests.get('http://text-processing.com/api/sentiment/', params=params)
            #     # TODO:
            j = resp.json()
            EntryClassification.objects.create(
                entry=e,
                negative=j['probability']['neg'],
                positive=j['probability']['pos'],
                neutral=j['probability']['neutral'],
                label=j['label']
            )
            e.analysis = True
            e.save()
