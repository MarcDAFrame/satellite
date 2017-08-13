"""
The main module for satellite
"""
from scrape import get_image
from PIL import Image


def get_and_crop(x_pos, y_pos, file_name):
    """
    Gets an image and crops out the google border thing

    @param {number} y_pos - The y position to get the image from
    @param {number} x_pos - The x positon to get the image from
    @param {string} file_name - The file name for the image to be saved to
    """
    get_image(y_pos, x_pos, file_name)
    img = Image.open(file_name)
    img = img.crop((0, 0, 640, 620))
    img.save(file_name)

def box_getter(box):
    """
    Gets all the images from a given box and downloads them

    @param {dict} - The range to get for the image

    @returns {void}
    """

    x_pos = box['x1']
    y_pos = box['y1']
    total_x = 0
    total_y = 0
    while True:
        if x_pos >= box['x1'] and x_pos <= box['x2']:
            if y_pos <= box['y1'] and y_pos >= box['y2']:
                get_and_crop(x_pos, y_pos, 'images/toronto/' + str(total_x) + ' ' + str(total_y) + '.png')
                x_pos += 0.00172
                total_x += 1
            else:
                break
        else:
            # x+=0.00165
            x_pos = box['x1']
            y_pos -= 0.0012
            total_y += 1
            total_x = 0

box_getter({'x1': -79.4062, 'x2': -79.4029, 'y1': 43.6515, 'y2': 43.64870})
