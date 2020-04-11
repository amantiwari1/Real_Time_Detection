from keras.models import load_model
import glob
import cv2
import numpy as np
import os

print("________________________LOADING...______________________")
names  = [] 
a = glob.glob("image/*")
b = " ".join(a).split(" ")
for i in b:
	names.append(i.split('\\')[1])


model = load_model("model.h5")

os.system("clear")
print("\t\t\n________________________Starting Real Time....______________________\t\t\n")


cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	face = cv2.resize(frame, (128, 128))
	a= np.argmax(model.predict(face.reshape(1,128,128,3)))

	x = names[a]
	face = cv2.resize(face , (500,500))
	cv2.putText(face, str(x), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

	cv2.imshow("hii", face)

	if cv2.waitKey(1)==13:
	    break
cap.release()
cv2.destroyAllWindows()