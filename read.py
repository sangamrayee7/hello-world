import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:\\Users\\Lenovo\\Pictures\\dog.jpg")
cv2.imwrite("C:\\Users\\Lenovo\\Pictures\\dog1.jpg",img)
 
# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#Displaying image using plt.imshow() method
plt.imshow(RGB_img)
 
# hold the window
plt.waitforbuttonpress()
plt.close('all')
