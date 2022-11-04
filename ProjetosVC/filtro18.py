import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('frutas.jpg',0)
plt.hist(img_bgr.ravel(),256,[0,256])
cv2.imshow("Imagem Original", img_bgr)
plt.show()
cv2.waitkey()