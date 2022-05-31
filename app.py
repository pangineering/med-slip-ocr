from Modules.detect_module import Detect


model_path="models/model.pt"

detect = Detect(model_path=model_path,yolo='custom')

img = 'Images/p97pnrb8m11rRObnjEt-o.jpg' 

detect.run(img)