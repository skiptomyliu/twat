
import flickr_api
from flickr_api import Walker, Photo
import config
import time

class FlickAPI(object):

    def __init__(self):
        flickr_api.set_keys(api_key=config.FLICKR_API_KEY, api_secret=config.FLICKR_SECRET)

    def get_recent(self):
        for i in range(5):
            photo = Photo.getRecent()[0]
            print photo.getInfo()['safety_level']
            if photo.getInfo()['safety_level'] == '0':
                if 'Large' in photo.getSizes():
                    tag = ""
                    if len(photo.getTags()):
                        tag = "#"+photo.getTags()[0].text
                    return (photo.getSizes()['Large']['source'], tag)
                print 'No Large'
            time.sleep(5)

    def get_photos(self):

        w = Walker(Photo.search, tags="sunset")
        # import pdb; pdb.set_trace()
        for photo in w[:2]:
            print photo.title  
            print photo.getSizes()['Large']['source']
            # import pdb; pdb.set_trace()


