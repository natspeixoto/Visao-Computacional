import cv2
 
catFaceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalcatface.xml')
 
image = cv2.imread('gato.jpg')
 
faces = catFaceCascade.detectMultiScale(image)
 
if len(faces) == 0:
    print("Nenhuma face encontrada")
 
else:
    print("Numero de faces localizadas: " + str(faces.shape[0]))
 
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))
 
    cv2.imshow('Imagem com as faces encontradas', image)
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
 
    cv2.destroyAllWindows()