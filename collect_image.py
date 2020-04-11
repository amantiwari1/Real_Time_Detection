import cv2
import numpy as np
import time
import os
from os import path

from config import n, max1

print("________________________LOADING...______________________")

os.mkdir("image")

for i in range(n):

	os.system("clear")

	print("________________________________________________")

	name = input("Enter Your Name (DO NOT SPACE) Only ONE Word :")
	print("________________________________________________\n\n")


	print("____________________LOADING...________________")


	cap = cv2.VideoCapture(0)

	input("are you ready for take Pic,"+name+"?")

	count = 0
	start = True
	while start:
		file_name = r'image/'+name

		if not path.isdir(file_name):
			os.mkdir(file_name)
			pass
		

		ret, frame = cap.read()
		count += 1
		face = cv2.resize(frame, (128, 128))



	    # Save file in specified directory with unique name
		file_name_path = file_name +'/'+ name + '.' + str(count) + '.jpg'
		cv2.imwrite(file_name_path, face)

	    # Put count on images and display live count
		cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
		face = cv2.resize(face, (600,600))
		cv2.imshow('Face Cropper', face)

		if cv2.waitKey(1) == 13 or count == max1: #13 is the Enter Key
		    start = False
        
	cap.release()
	cv2.destroyAllWindows()
	os.system("clear")

print("Collecting Samples Complete")