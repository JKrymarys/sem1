import numpy as np
import cv2
import utils

def average_filter(img):
    new_image = img.copy()
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
    chanels = [b,g,r]
    chanel_no = 0
    for c in chanels:
        print(c)
        n = 0
        average_sum = 0
        for i in range(0, len(c)):
            for j in range(0, len(c[i])):
                for k in range(-2, 3):
                    for l in range(-2, 3):
                        if (len(c) > (i + k) >= 0) and (len(c[i]) > (j + l) >= 0):
                            average_sum += c[i+k][j+l]
                            n += 1
                print(chanel_no)
                new_image[i][j][chanel_no] = (int(round(average_sum/n)))
                average_sum = 0
                n = 0
        chanel_no += 1
    return new_image


def calculate_median(image, x, y, c):
    temp = 0
    temp_arr = []
    median_value = []
    median_range = [-1,0,1,]
    if x > 0 and x < 255 and y > 0 and y < 255:
        print(image[x][y][c])
        for i in median_range:
            for j in median_range:
                temp_arr.append(image[x+i][y+j][c])
                print ("temp-arr: ", temp_arr)

        temp_arr.sort()
        median_value = temp_arr[4]
        print ("HERE", temp_arr)  
    else:
        print("not changing: ", image[x][y][c])
        median_value = image[x][y][c]
        
    return median_value
    


def median_filter_2(img):
    new_image = img.copy()
    img_height = utils.get_image_height(img)
    img_width = utils.get_image_width(img)

    for y in range(img_height):
        for x in range(img_width):
            for c in range(3):
                new_image[x][y][c] = calculate_median(img, x, y, c)
    
    return new_image


def median_filter(img, filter_size):
    new_image = img.copy()
    temp = []
    indexer = filter_size // 2
    img_height = utils.get_image_height(img)
    img_width = utils.get_image_width(img)
    for y in range(img_height):
        for x in range(img_width):
            for c in range(3):
                for z in range(filter_size):
                    if y + z - indexer < 0 or y + z - indexer > img_height - 1:
                        temp.append(0)
                    else:
                        if x + z - indexer < 0 or x + indexer > img_width - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(img[y + z - indexer][x + k - indexer][c])
                    temp.sort()
                    new_image[y][x][c] = temp[len(temp) // 2]
                    temp = []
    return new_image