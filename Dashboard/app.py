import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from Modules.detect_module import Detect
from Modules.manage_data_module import Dataset


st.title('Read the Med Slip')
# Include PIL, load_image before main()


def load_image(image_file):
	img = Image.open(image_file)
	return img

model_path="models/model.pt"



st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:
    # To See details
	file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
	st.write(file_details)

    # To View Uploaded Image
	st.image(load_image(image_file),width=250)


detect = Detect(model_path=model_path,yolo='custom')

#img = 'Images/p97pnrb8m11rRObnjEt-o.jpg' 
#img_1 = im.open(img)
img_data = Dataset(img_file="Images/")

img_list = img_data.readImage()

detect.run(img_list)

 # To View Uploaded Image
st.image(load_image(image_file),width=250)