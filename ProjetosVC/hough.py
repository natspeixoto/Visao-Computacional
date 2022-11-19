import cv2
import numpy as np 

img = cv2.imread('estrada.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3) # primeiro converte em cinza
lines = cv2.HoughLines(edges,1,np.pi/180, 200)
for r, theta in lines[0]:

    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*r
    y0 = b*r
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 100*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)

cv2.imwrite('estrada.jpg', img)    

# quando a imagem é muito colorida, é difícil identificar as linhas. Testar outras imagens. No meu primeiro teste ficou uó.
# Estava dando erro, para consertá-lo, foi necessário instalar o python no app local já que na Fatec não é possível instalar no C:
# Depois, instalar as bibliotecas pelo terminal vo vsc "pip install opencv-python" e depois "pip install numpy". Reinicia o visual code e zás!
