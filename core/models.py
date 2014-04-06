from django.core.urlresolvers import reverse
from django.db import models
from TwitterSearch import TwitterSearch, TwitterSearchOrder, TwitterSearchException
from django.conf import settings

# Create your models here.
from urllib import quote_plus


class EntryQueue(models.Model):
    origin = models.CharField(max_length=200)
    origin_id = models.BigIntegerField(blank=True)
    message = models.TextField(blank=True)
    author_id = models.BigIntegerField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    areas = models.ManyToManyField('Area')
    analysis = models.BooleanField(default=False)
    datetime = models.DateTimeField(null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    class Meta:
        unique_together = ('origin', 'origin_id',)

    def classification(self):
        classif = self.entryclassification_set.all()[0].label
        return classif


class EntryClassification(models.Model):
    entry = models.ForeignKey('EntryQueue')
    positive = models.FloatField(null=True)
    negative = models.FloatField(null=True)
    neutral = models.FloatField(null=True)
    label = models.CharField(max_length=20, blank=True)

class ApiRequests(models.Model):
    name = models.CharField(max_length=20)
    url = models.TextField()
    counter = models.IntegerField()
    until = models.DateTimeField()



def save_tweets(area, origin, tweet):
    result = None
    coordinates_key = 'coordinates'
    # try:
    #     import ipdb;ipdb.set_trace()
    if coordinates_key in tweet and tweet[coordinates_key] and 'type' in tweet[coordinates_key] and tweet[coordinates_key]['type'] == 'Point' and coordinates_key in tweet[coordinates_key] and tweet[coordinates_key][coordinates_key]:
        coord_lat = tweet[coordinates_key][coordinates_key][1]
        coord_long = tweet[coordinates_key][coordinates_key][0]
        eq, created = EntryQueue.objects.get_or_create(
            origin=origin.name,
            origin_id=tweet['id'],
            defaults={
                'message': tweet['text'],
                'author_id': tweet['user']['id'],
                'lat': coord_lat,
                'long': coord_long
            }
        )
        eq.save()
        area.entryqueue_set.add(eq)
        result = tweet['id']
    else:
        eq, created = EntryQueue.objects.get_or_create(
            origin=origin.name,
            origin_id=tweet['id'],
            defaults={
                'message': tweet['text'],
                'author_id': tweet['user']['id']
            }
        )
        area.entryqueue_set.add(eq)
        result = tweet['id']
    print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
    # except Exception as ex:
    #     print ex.message
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
    return result


class Area(models.Model):
    description = models.CharField(max_length=200)
    lat = models.FloatField(blank=True)#
    long = models.FloatField(blank=True)#
    rad = models.PositiveIntegerField(blank=True)

    def __unicode__(self):
        return self.description


class SourceForArea(models.Model):
    name = models.CharField(max_length=30)
    area = models.ForeignKey('Area')
    since_id = models.BigIntegerField(null=True, blank=True)
    max_id = models.BigIntegerField(null=True, blank=True)

    def fetch_new_twitter_entries(self):
        # read since_id
        pass

    def fetch_twitter_entries(self):
        origin = self
        max_id = origin.max_id
        since_id = None
        area = origin.area
        try:
            count = 50
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.setKeywords(['']) # let's define all words we would like to have a look for
            tso.setResultType('recent')
            if origin.max_id:
                tso.setMaxID(origin.max_id-1)  # as per twitter docs
            tso.setLanguage('en') # we want to see German tweets only
            tso.setGeocode(latitude=area.lat, longitude=area.long, radius=area.rad, km=True)
            tso.setCount(count) # please dear Mr Twitter, only give us 7 results per page
            tso.setIncludeEntities(False) # and don't give us all those entity information

            # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                **settings.TWITTER
            )
            total = 0
            for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)

                max_id = save_tweets(area, origin, tweet)
                if not since_id:
                    since_id = max_id

                #import ipdb;ipdb.set_trace()
                #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

                total += 1

                if total >= 50:
                    break

        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)
        # except:
        #     pass
        finally:
            origin.max_id = max_id
            origin.save()