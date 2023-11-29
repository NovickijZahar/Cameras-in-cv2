import cv2
import pyautogui
import numpy as np

result = cv2.VideoWriter('screencapture.avi', cv2.VideoWriter_fourcc(*'MJPG'), 13, pyautogui.size())

while True:
    cv2.namedWindow('Screen capture', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Screen capture', 800, 600)
    img = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    result.write(frame)
    cv2.imshow('Screen capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

result.release()
cv2.destroyAllWindows()