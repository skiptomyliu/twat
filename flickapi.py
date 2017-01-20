
import flickr_api
from flickr_api import Walker, Photo
import config 

class FlickAPI(object):

    def __init__(self):
        flickr_api.set_keys(api_key=config.FLICKR_API_KEY, api_secret=config.FLICKR_SECRET)

    def get_recent(self):
        return Photo.getRecent()[0].getSizes()['Large']['source']
        
    def get_photos(self):

        import pdb; pdb.set_trace()

        w = Walker(Photo.search, tags="sunset")
        # import pdb; pdb.set_trace()
        for photo in w[:1]:
            print photo.title  
            print photo.getSizes()['Large']['source']
            # import pdb; pdb.set_trace()


