import easyocr
import PIL
from PIL import ImageDraw
#import pandas as pd
import cv2



class Read_text:
    def __init__(self,img):
        self.imgs = img

    def easy_read(self):

        print(len(self.imgs))

        reader = easyocr.Reader(['en','en'])

        result = []

        for img in self.imgs:
            #print(len(img))
            temp = []
            for i in img:
                if i == "None":
                    temp.append("None")
                else:
                    bounds = reader.readtext(i,detail = 0)
                    temp.append(bounds)
            result.append(temp)
                

        return result


    def data2dict(self):
        row = []
        
        i = 0
        temps = self.easy_read()
        

        return row

    def print_data(self):
        results = self.easy_read()

        #for result in results:
        #    print(result[0][0])
        #    print(result[3][0])
        #    print(result[4][0])
        #    print("-----------------------------")

        print(results)
