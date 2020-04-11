import cv2
import numpy as np
import time
import os
from os import path
import glob
from config import n, max2
import time



names  = [] 
a = glob.glob("image/*")
b = " ".join(a).split(" ")
for i in b:
    names.append(i.split('\\')[1])

input("\t\t\n\n DATA COLLECT FOR IMAGE TEST  \n enter continue...")


os.mkdir("image_test")

for i in range(n):
    name = names[i]
    print("__________loading________________")
    cap = cv2.VideoCapture(0)

    input("are you ready for take Pic,"+name+"?")
    

    count = 0
    start = True
    while start:
        file_name = r'image_test/'+name

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

        if cv2.waitKey(1) == 13 or count == max2: #13 is the Enter Key
            start = False
        
    cap.release()
    cv2.destroyAllWindows()
    os.system("clear")

print("Collecting Samples Complete")

print("\n\n\n____________________Successfully collected images________________\n\n\n")

time.sleep(1)
