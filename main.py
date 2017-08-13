from scrape import get_image
from PIL import Image


def get_and_crop(x,y,file_name):
    get_image(y, x, file_name)
    img = Image.open(file_name)
    img = img.crop((0,0, 640, 620))
    img.save(file_name)

def box_getter():
    #box = {'x1' : -79.4180, 'x2' : -79.3200, 'y1' : 43.6743, 'y2' : 43.6311}
    box = {'x1' : -79.4062, 'x2' : -79.4029, 'y1' : 43.6515, 'y2' : 43.64870}
    x = box['x1']
    y = box['y1']
    total_x = 0
    total_y = 0
    while True:
        if x >= box['x1'] and x <= box['x2']:
            if y <= box['y1'] and y >= box['y2']:
                #print(x, y)
                get_and_crop(x,y,'images/toronto/'+str(total_x)+' '+str(total_y)+'.png')
                x+=0.00172
                total_x+=1
            else:
                break
        else:
            # x+=0.00165
            x = box['x1']
            y-=0.0012
            total_y+=1
            total_x=0

box_getter()