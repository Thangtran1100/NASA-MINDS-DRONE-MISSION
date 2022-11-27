import cv2
from djitellopy import Tello
import keyboard as key
import os
import time

global image

width = 320
height = 240
startCounter = 0

drone = Tello()
drone.connect()
print(drone.get_battery())


dir_path = 'D:\\NASA-MINDS-DRONE-MISSION\\11_18_2022\\image-capture'
#os.makedirs(dir_path, exist_ok=True)
#base_path = os.path.join(dir_path, base)
n = 0

drone.streamon()

# 0: forward camera
# 1: bottom camera
#drone.set_video_direction(0)

#drone.takeoff()

while True:
    image = drone.get_frame_read().frame
    #img = cv2.resize(img, (360,240))
    
    cv2.imshow('Figure 1', image)
    cv2.waitKey(0)
    cv2.show()
    
    # drone.rotate_clockwise(90)
    # time.sleep(3)
    # drone.move_left(35)
    # time.sleep(3)
    # if cv2.waitKey(32) == ord('Space'):
    #     drone.land()
    #     break
    
    # if key.read_key() == 'space':
    #     drone.land()
    #     break
    cv2.imwrite(f'D:\\NASA-MINDS-DRONE-MISSION\\11_18_2022\\image-capture\\{time.time()}.jpg', image)
    
cv2.destroyAllWindows()