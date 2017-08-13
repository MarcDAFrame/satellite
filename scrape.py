import os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def get_image(y,x,file_name):
    #"https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.9987&zoom=19&size=1000x1000&maptype=satellite"
    url = "https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=19&size=1000x1000&maptype=satellite" % (y,x)
    print(url)
    urlretrieve(url, file_name)

# get_image(40.714728, -73.9987, 'image.png')
# get_image(43.6532, -79.3832, 'test.png')
# get_image(41, -73, 'bad.png')

