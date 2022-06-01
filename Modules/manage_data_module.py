import cv2
import PIL
from PIL import Image as im
from PIL import ImageDraw
import os

# Load data
class Dataset:
    def __init__(self,img_file=""):
        self.img_path = img_file


    def readImage(self):
        # Get images into array
        img_file = []
        for filename in os.listdir(self.img_path):
            f = os.path.join(self.img_path, filename)
            # checking if it is a file
            if os.path.isfile(f):
                img_file.append(f)

        return img_file


    def showImage(self):
        pass

    def saveImage(self):
        pass


class Output:
    pass
        