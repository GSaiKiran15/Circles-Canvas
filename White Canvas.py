import numpy as np
import cv2

canvas = np.ones((800,800,3), 'uint8')*255

center = (100,100)
color = (0,0,255)
radius = 100
thickness = 3
pressed = False
def mouse_click(event, x,y,flags,params):
    global center, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        center = x,y
        pressed = True
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas, (x,y), radius, color, thickness)
    elif event == cv2.EVENT_LBUTTONDOWN:
        pressed = False
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", mouse_click)

while True:
    cv2.circle(canvas, center, radius, color, thickness)
    cv2.imshow("Canvas", canvas)
    ch = cv2.waitKey(1)
    if ch == ord('b'):
        color = (255, 0, 0)
    elif ch == ord('g'):
        color = (0,255, 0)
    elif ch == ord('r'):
        color = (0,0,255)
    elif ch == ord('q'):
        break
canvas.release()
cv2.destroyAllWindows()