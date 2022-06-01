import cv2
from Modules.manage_data_module import Dataset
from Modules.detect_module import Detect
from Modules.ocr_module import Read_text
from PIL import Image as im

model_path="models/model.pt"

detect = Detect(model_path=model_path,yolo='custom')


#img = 'Images/p97pnrb8m11rRObnjEt-o.jpg' 
#img_1 = im.open(img)
img_data = Dataset(img_file="Images/")

img_list = img_data.readImage()

detect.run(img_list)

#result = ["runs/detect/exp6/crops/sys/p97pnrb8m11rRObnjEt-o.jpg"]

#read = Read_text(img=result)

#res = read.easy_read()

print(detect)