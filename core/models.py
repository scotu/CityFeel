from django.db import models
from TwitterSearch import TwitterSearch, TwitterSearchOrder, TwitterSearchException
from django.conf import settings

# Create your models here.
class EntryQueue(models.Model):
    message = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    area = models.ForeignKey('Area')
    original = models.TextField(blank=True)
    analysis = models.BooleanField()

    def fetch_entries(self):
        try:
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.setKeywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
            tso.setLanguage('en') # we want to see German tweets only
            tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
            tso.setIncludeEntities(False) # and don't give us all those entity information

            # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                **settings.TWITTER
             )

            for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
                print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)

class Area(models.Model):
    description = models.CharField(max_length=200)
