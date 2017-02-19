


from twitterapi import TwitterAPI
from flickapi import FlickAPI
from shapes import grid
import urllib
from random import randint

twatapi = TwitterAPI()
flickapi = FlickAPI()

img_url = flickapi.get_photos()
# img_url, _ = flickapi.get_recent()
print img_url
urllib.urlretrieve(img_url, "recent.JPEG")

pix_multis = [".011", ".014", ".018"]
grid = grid.Grid("recent.JPEG", pix_multi=pix_multis[randint(0,2)], diamond=True, colorful=True, enlarge=2500)
grid.n_pass()
grid.save("out.JPEG")

#twatapi.post_image("out.JPEG", ["#mosaic", "#mosaicshapes", "#art", "#mosaicart"])
