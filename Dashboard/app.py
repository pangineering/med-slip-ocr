from charset_normalizer import detect
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from Modules.detect_module import Detect
from Modules.manage_data_module import Dataset, Output
import time
from Modules.ocr_module import Read_text

st.title('Read the Med Slip')
# Include PIL, load_image before main()


def load_image(image_file):
	img = Image.open(image_file)
	return img

model_path="models/best.pt"

def read_slip(model,img):
	detect = Detect(model_path=model,yolo='custom')
	detect.run(img)
	output = Output(img_file="runs/detect/")
	out_dir = output.loop_crop()
	read = Read_text(img=out_dir)
	res = read.easy_read()

	return res


st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"],accept_multiple_files=True)

if image_file is not None:
    # To See details
	#file_details = {"filename":image_file.name, "filetype":image_file.type,
                            #  "filesize":image_file.size}
	#st.write(file_details)

    # To View Uploaded Image
	#st.image(load_image(image_file),width=250)


	#detect = Detect(model_path=model_path,yolo='custom')

	
	
	#img_1 = im.open(img)
	#img_data = Dataset(img_file="Images/")

	#img_list = img_data.readImage()

	#detect.run(img_list)
	with st.spinner(text='In progress'):
			time.sleep(5)
			st.success('Done')
	
	result = []
	# To View Uploaded Image
	for img_file in image_file:
		img = load_image(img_file)
		st.image(img,width=250)

		res = read_slip(model_path,img)

		result.append(res)

	

	row = []

	for data in result:
		new_result = []
		dat = data[0]
		
		if len(dat) > 1:
			date = ""
			for d in dat:
				date = date + d

		else:
			date = dat[0]
		
		time_ = data[1][0][0]
		sys = data[2][0][0]
		dia = data[3][0][0]
		pul = data[4][0][0]

		new_result.append(date)
		new_result.append(time_)
		new_result.append(sys)
		new_result.append(dia)
		new_result.append(pul)

		row.append(new_result)

	#st.write(row)

	df  = pd.DataFrame(row,columns=['date','time','sys','dia','pul'])
	
	# sys = []
	# for r in res[2]:
	# 	sys.append(r[0])
	# dia = []
	# for r in res[3]:
	# 	dia.append(r[0])
	# pul = []
	# for r in res[4]:
	# 	pul.append(r[0])
	# t = []
	# for r in res[1]:
	# 	t.append(r[0])

	# df['date'] = res[0]
	# df['time'] = t
	# df['sys'] = sys
	# df['dia'] = dia
	# df['pul'] = pul

	st.dataframe(df)