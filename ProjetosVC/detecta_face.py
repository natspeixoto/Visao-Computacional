# Python MediaPipe: estimativa de marcos faciais
import cv2
import mediapipe
 
drawingModule = mediapipe.solutions.drawing_utils
faceModule = mediapipe.solutions.face_mesh
 
circleDrawingSpec = drawingModule.DrawingSpec(
    thickness=1, circle_radius=1, color=(0, 255, 0))
lineDrawingSpec = drawingModule.DrawingSpec(thickness=1, color=(0, 255, 0))
 
with faceModule.FaceMesh(static_image_mode=True) as face:
    image = cv2.imread('face.jpg')
 
    results = face.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
 
    if results.multi_face_landmarks != None:
        for faceLandmarks in results.multi_face_landmarks:
            drawingModule.draw_landmarks(
                image, faceLandmarks, faceModule.FACEMESH_TESSELATION, circleDrawingSpec, lineDrawingSpec)
 
    cv2.imshow('Detecção dos pontos geoometricos face', image)
 
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
 
    cv2.destroyAllWindows()

# Foi adicionado ao diretório do projeto um conjunto de algoritmos (haarcascades) que faz estes mapeamentos 
# Além de instalar o mediapipe