import cv2
from Modules.manage_data_module import Dataset, Output
from Modules.detect_module import Detect
from Modules.ocr_module import Read_text
from PIL import Image as im
import pandas as pd




model_path="models/best.pt"

detect = Detect(model_path=model_path,yolo='custom')


#img = 'Images/p97pnrb8m11rRObnjEt-o.jpg' 
#img_1 = im.open(img)
img_data = Dataset(img_file="Images/")

img_list = img_data.readImage()

detect.run(img_list)

#result = ["runs/detect/exp6/crops/sys/p97pnrb8m11rRObnjEt-o.jpg"]



output = Output(img_file="runs/detect/")

out_dir = output.loop_crop()

print(out_dir)




read = Read_text(img=out_dir)
res = read.easy_read()
print(res)
df  = pd.DataFrame(columns=['sys','dia','pul'])

df['date'] = res[0]
df['time'] = res[1]
df['sys'] = res[2]
df['dia'] = res[3]
df['pul'] = res[4]

df.to_csv('data.csv',index=True)

