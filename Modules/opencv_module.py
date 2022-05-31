from imutils.perspective import four_point_transform
import argparse
import imutils
import cv2
import re

# Importing Image module from PIL package 
from PIL import Image 
import PIL 


class detect_slip:
    def __init__(self,image_file=""):
        self.orig = cv2.imread(image_file)
        image = self.orig.copy()
        self.image = imutils.resize(image, width=500)
        self.ratio = self.orig.shape[1] / float(image.shape[1])

    def detect_edge(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
        edged = cv2.Canny(blurred, 75, 200)
        # check to see if we should show the output of our edge detection
        # procedure
        #if args["debug"] > 0:
        cv2.imshow(self.image)
        cv2.imshow(edged)

    def get_contour(self):
        # initialize a contour that corresponds to the receipt outline
        receiptCnt = None
        # find contours in the edge map and sort them by size in descending
        # order
        cnts = cv2.findContours(self.edged.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        # loop over the contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # if our approximated contour has four points, then we can
            # assume we have found the outline of the receipt
            if len(approx) == 4:
                receiptCnt = approx
                break
        # if the receipt contour is empty then our script could not find the
        # outline and we should be notified
        if receiptCnt is None:
            raise Exception(("Could not find receipt outline. "
                "Try debugging your edge detection and contour steps."))


        # check to see if we should draw the contour of the receipt on the
        # image and then display it to our screen

        output = self.image.copy()
        cv2.drawContours(output, [receiptCnt], -1, (0, 255, 0), 2)
        cv2.imshow(output)


        # apply a four-point perspective transform to the *original* image to
        # obtain a top-down bird's-eye view of the receipt
        receipt = four_point_transform(self.orig, receiptCnt.reshape(4, 2) * self.ratio)
        # show transformed image
        cv2.imshow(imutils.resize(receipt, width=500))

        return output

        
    def save_crop_edge_img(self):
        pass

    def save_temp_image(self,img,class_name,img_id):
        path = 'temp_img/'

        img = img.save(path + img_id + '_' + class_name + '.jpg')
        

