import easyocr
import pytesseract
import PIL
from PIL import ImageDraw
import pandas as pd
import cv2

class read_text:

    def easy_read():
        pass

    def tess_read():
        options = "--psm 4"
        text = pytesseract.image_to_string(
            cv2.cvtColor(receipt, cv2.COLOR_BGR2RGB),
            config=options)
        # show the raw output of the OCR process
        print("[INFO] raw output:")
        print("==================")
        print(text)
        print("\n")

    # Draw bounding boxes
    def draw_boxes(self,image, bounds, color='yellow', width=2):
        draw = ImageDraw.Draw(image)
        for bound in bounds:
            p0, p1, p2, p3 = bound[0]
            draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
        return image

    def data2dict(self):
        data = dict()

        return data

    def export_csv(self):
        pass
