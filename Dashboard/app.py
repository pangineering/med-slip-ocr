from charset_normalizer import detect
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from Modules.detect_module import Detect
from Modules.manage_data_module import Dataset, Output
import time
from Modules.ocr_module import Read_text
from Modules.date_module import Clean_Date
from datetime import date

today = date.today()
file_name = 'data_' + str(today)+'.csv'
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
	
	result = []

	# To View Uploaded Image
	for img_file in image_file:
		img = load_image(img_file)
		
		st.image(img,width=200)
	

	#for img_file in image_file:	
		res = read_slip(model_path,img)

		result.append(res)
		
	if result != []:	

		my_bar = st.progress(0)

		#for percent_complete in range(100):
		#	time.sleep(0.09)
		#	my_bar.progress(percent_complete + 1)

		row = []

		for data in result:
			new_result = []
			date_ = []
			dat = data[0]
			
			if len(dat[0]) > 1:
				date_1 = Clean_Date(date_string=dat[0])

				date = date_1.formatDate()
				

			else:
				date = dat[0][0]
			
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


		df  = pd.DataFrame(row,columns=['date','time','sys','dia','pul'])
		

			
		st.dataframe(df)

		@st.cache
		def convert_df(df):
			# IMPORTANT: Cache the conversion to prevent computation on every rerun
			return df.to_csv().encode('utf-8')

		csv = convert_df(df)

		st.download_button(
			label="Download data as CSV",
			data=csv,
			file_name=file_name,
			mime='text/csv',
	)