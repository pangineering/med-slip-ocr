import cv2
import PIL
from PIL import Image as im
from PIL import ImageDraw

# Load data
class Dataset:
    def __init__(self,img_file="",qty="single"):
        self.img_path = img_file
        self.qty = qty #'single' for one image and 'multi' for more than one

    def readImage(self):
        if self.qty=="single":
            pass
        else:
            pass

    def showImage(self):
        if self.qty=="single":
            pass
        else:
            pass

    def saveImage(self):
        if self.qty=="single":
            pass
        else:
            pass

        