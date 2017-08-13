"""
The module to get the images from google
"""
from urllib.request import urlretrieve


def get_image(y_pos, x_pos, file_name):
    """
    Downloads a segment of the map image

    @param {number} y_pos - The y position for the map segment
    @param {number} x_pos - The x position for the map segment
    @param {string} file_name - The name that the file will be saved under
    """

    url = "https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=19&size=1000x1000&maptype=satellite" % (y,x)
    print(url)
    urlretrieve(url, file_name)

# get_image(40.714728, -73.9987, 'image.png')
# get_image(43.6532, -79.3832, 'test.png')
# get_image(41, -73, 'bad.png')
