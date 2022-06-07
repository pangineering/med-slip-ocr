import cv2
import PIL
from PIL import Image as im
from PIL import ImageDraw
import os
from natsort import natsorted

# Load data


class Dataset:
    def __init__(self, img_file=""):
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
    def __init__(self, img_file=""):
        self.img_path = img_file




    def get_dir(self):
        exp_dirs = []
        for filename in os.listdir(self.img_path):
            f = os.path.join(self.img_path, filename)
            # checking if it is a directory
            if os.path.isdir(f):                    
                exp_dirs.append(f)

        
        list = natsorted(exp_dirs)
        latest = len(list) - 1
        return list[latest]

    def loop_crop(self):
        crops = []
        data = ['date','time','sys','dia','pul']
        target = self.get_dir() + '/crops/'
        for d in data:
            t = target + d
            temp = []
            if os.path.isdir(t): 
                for filename in os.listdir(t):
                
                    f = os.path.join(t, filename)
                    # checking if it is a directory
                    if os.path.isfile(f):
                        temp.append(f)
                    else:
                        temp.append("None")
                        print("None")
                        

                crops.append(temp)

        return crops


