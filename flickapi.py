
import flickr_api
from flickr_api import Walker, Photo
import config
import time
from random import randint

class FlickAPI(object):

    def __init__(self):
        flickr_api.set_keys(api_key=config.FLICKR_API_KEY, api_secret=config.FLICKR_SECRET)

    def get_recent(self):
        for i in range(5):
            photo = Photo.getRecent()[0]
            if photo.getInfo()['safety_level'] == '0':
                if 'Large' in photo.getSizes():
                    tag = ""
                    if len(photo.getTags()):
                        tag = "#"+photo.getTags()[0].text
                    return (photo.getSizes()['Large']['source'], tag)
                print 'No Large'
            time.sleep(5)

    def get_photos(self):
        random_tags = ['sunset', 'animals', 'portrait', 
            'beach', 'sunrise', 'sport', 'water', 'summer', 
            'winter', 'spring', 'bird']

        walker = Walker(Photo.search, tags=random_tags[randint(0, len(random_tags)-1)])
        photos = walker._curr_list
        for i in range(5):
            idx = randint(0, len(photos)-1)
            photo = photos[idx]
            if photo.getInfo()['safety_level'] == '0':
                if 'Large' in photo.getSizes():
                    return photo.getSizes()['Large']['source']

                print 'No Large'
            time.sleep(5)
