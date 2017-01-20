


from twitterapi import TwitterAPI
from flickapi import FlickAPI
from shapes import grid
import urllib
from random import randint

twatapi = TwitterAPI()
flickapi = FlickAPI()
# twatapi.post_image("/Users/dliu/Desktop/moi.JPEG")

img_url, tag = flickapi.get_recent()
print img_url
urllib.urlretrieve(img_url, "recent.JPEG")

pix_multis = [".01", ".014", ".02"]
grid = grid.Grid("recent.JPEG", pix_multi=pix_multis[randint(0,2)])
grid.n_pass()
grid.save("out.JPEG")

twatapi.post_image("out.JPEG", ["#mosaic", "#mosaicshapes", "#art", "#mosaicart" tag])