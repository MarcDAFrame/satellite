import cv2
import numpy as np
import os.path
# img = cv2.imread('img.png')
# vis = np.concatenate((img1, img2), axis=1)
# cv2.imwrite('out.png', vis)






def combine_images(file_dir):
    #dirs = [d for d in os.listdir(file_dir) if os.path.isdir(os.path.join(file_dir, d))]
    # print(os.listdir(file_dir))
    break_now = False
    current_y = 0
    current_x = 0
    images = [[]]
    visuals = []

    print(cv2.imread('./images/toronto/0 0.png'))

    while True:
        path = str(current_x) + ' ' + str(current_y) + '.png'
        if os.path.exists(file_dir + path):
            print(file_dir + path)
            images[current_y].append(cv2.imread(file_dir + path))
            break_now = False
            current_x += 1
        else:
            if break_now:
                images = images[:-1]
                break

            break_now = True
            images.append([])
            current_x = 0
            current_y += 1

    for image_row in images:
        visuals.append(np.concatenate(image_row, axis=1))
    vis = np.concatenate(visuals, axis=0)
    cv2.imwrite(file_dir + '1out.png', vis)
        
    


combine_images('./images/toronto/')