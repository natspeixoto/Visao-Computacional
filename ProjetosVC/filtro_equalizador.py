from matplotlib import pyplot as plt
import cv2

img = cv2.imread('frutas.jpg',0)
img = img[::2,::2] #altera tamanho da imgem
h_eq = cv2.equalizeHist(img)

#altera o tammanho do Histograma
plt.figure("histograma Original", figsize=(3,3))
plt.title("Histograma Original", fontsize=15)
plt.xlabel("Instesidade", fontsize=15)
plt.ylabel("Quantidade de Pixels",fontsize=15)
plt.tick_params(labelsize=15)

plt.hist(img.ravel(),256,[0,256])
plt.xlim([0,256])
cv2.imshow("Imagem Origianl", img)

#Altera o tamanho do histograma

plt.figure("histograma Equalizador", figsize=(3,3))
plt.title("Histograma Equalizador", fontsize=15)
plt.xlabel("Instesidade", fontsize=15)
plt.ylabel("Quantidade de Pixels",fontsize=15)
plt.tick_params(labelsize=15)

plt.hist(h_eq.ravel(),256,[0,256],5, rwidth=0.9,
        color='blue', alpha=0.7, edgecolor='black')
plt.xlim([0,256])
cv2.imshow("Imagem Equalizada", h_eq)
plt.show()
cv2.waitKey(0)


