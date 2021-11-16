import cv2
import numpy as np

def draw(mask, color, frame_arg):
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        ar = cv2.contourArea(c)
        if ar > 1000:
            new_contour = cv2.convexHull(c)
            cv2.drawContours(frame_arg, [new_contour], 0, color, 3)


def capture():
    # Camara
    cap = cv2.VideoCapture(0)

    # **** COLORES *****

    # AMARILLO:

    #______________________________________________
    # Amarillo Suave
    low_yellow = np.array([25,190,20], np.uint8)
    # Amarillo Fuerte
    high_yellow = np.array([30,255,255], np.uint8)
    #______________________________________________

    # ROJO:

    #______________________________________________
    # Rojo suave rango 1
    low_red1 = np.array([0,100,20], np.uint8)
    # Rojo fuerte rango 1
    high_red1 = np.array([5,255,255], np.uint8)
    # Rojo suave rango 2
    low_red2 = np.array([175,100,20], np.uint8)
    # Rojo fuerte rango 2
    high_red2 = np.array([180,100,20], np.uint8)
    #______________________________________________

    while True:
        
        comp, frame = cap.read()
        if comp == True:
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            yellowMask = cv2.inRange(frame_HSV, low_yellow, high_yellow)
            redMask1 = cv2.inRange(frame_HSV, low_red1, high_red1)
            redMask2 = cv2.inRange(frame_HSV, low_red2, high_red2)
            redMask = cv2.add(redMask1,redMask2)

            # Dibuja Mascara Amarilla
            draw(yellowMask, [0,255,255], frame)
            # Dibuja Mascara Roja
            draw(redMask, [0,0,255], frame)

            cv2.imshow('Webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('Q'):
                break
            cap.release()
            cv2.destroyAllWindows()

