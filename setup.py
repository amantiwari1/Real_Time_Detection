import shutil
import os
if os.path.isdir("image"): 	
	shutil.rmtree("image") 
	
if os.path.isdir("image_test"):
	shutil.rmtree("image_test") 






import config
import collect_image
import collect_image_test
import train
import Real_Time

print("""                     


			\n\t\t\t\t\tYOU CAN RUN python 'Real_Time.py' AGAIN FOR REAL TIME VIDEO AFTER TRAINING
\t\t\t\t\n





	""")