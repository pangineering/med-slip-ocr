import easyocr
import PIL
from PIL import ImageDraw
#import pandas as pd
import cv2



class Read_text:
    def __init__(self,img):
        self.imgs = img

    def easy_read(self):
        reader = easyocr.Reader(['en','en'])

        result = []

        for img in self.imgs:
            bounds = reader.readtext(img,detail = 0)
            result.append(bounds)

        return result


    def data2dict(self):
        row = []
        data = dict()

        temp = self.easy_read()

        #data['date'] = date
        #data['time'] = temp[2][0].replace(" ", "")
        data['sys'] = temp[3][0]
        data['dia'] = temp[0][0]
        data['pul'] = temp[4][0]

        row.append(data)

        return row

    def print_data(self):
        results = self.easy_read()

        for result in results:
            print(result[0][0])
            print(result[3][0])
            print(result[4][0])
            print("-----------------------------")

    def export_csv(self):
        pass