import numpy as np
import cv2

def load_image(file_path):
    # Load an color image in grayscale
    img = cv2.imread(file_path,0)
    return img

def display_image(image_url):
    cv2.imshow("test",image_url)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#script
try:
    img = load_image('cat.jpg')
    display_image(img)
except Exception as e:
    print(f"exception: {e}")

#display_image(img)