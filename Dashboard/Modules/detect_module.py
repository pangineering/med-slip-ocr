import cv2
import torch
from PIL import Image

class Detect:
    def __init__(self,model_path,conf=0.30,yolo='yolov5s'):
        self.model_path = model_path #path to model
        self.conf = conf #default is 0.30
        self.yolo = yolo #default is yolov5s

    def load_model(self):
        if self.yolo == 'custom':
            model = torch.hub.load('ultralytics/yolov5', self.yolo, path=self.model_path)  # local model
        else:
            # Model
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        
        return model

    def run(self,img):
        model = self.load_model()
        model.conf = self.conf
        results = model(img)

        results.crop() #results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

        
