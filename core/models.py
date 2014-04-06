from django.db import models
from TwitterSearch import TwitterSearch, TwitterSearchOrder, TwitterSearchException
from django.conf import settings

# Create your models here.
from urllib import quote_plus


class EntryQueue(models.Model):
    origin = models.CharField(max_length=200)
    origin_id = models.CharField(max_length=500, blank=True)
    message = models.TextField(blank=True)
    author_id = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    area = models.ForeignKey('Area')
    original = models.TextField(blank=True)
    analysis = models.BooleanField()
    class Meta:
        unique_together = ('origin', 'origin_id',)




def fetch_entries():
    origin = 'twitter'

    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.setKeywords(['']) # let's define all words we would like to have a look for
        tso.setLanguage('en') # we want to see German tweets only
        tso.setGeocode(latitude=37.7599046, longitude=-122.4168468, radius=10, km=True)
        tso.setCount(10) # please dear Mr Twitter, only give us 7 results per page
        tso.setIncludeEntities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            **settings.TWITTER
         )

        import ipdb;ipdb.set_trace()
        for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
            EntryQueue.objects.create(
                origin=origin,
                origin_id=tweet['id_str'],
                message=tweet['text'],
                author_id=str(tweet['user']['id'])
            )
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)


class Area(models.Model):
    description = models.CharField(max_length=200)

