import cv2
import matplotlib.pyplot as plt
img= cv2.imread("‪C:\\Users\\Lenovo\\Pictures\\dog.jpg", cv2.IMREAD_COLOR)
plt.imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
