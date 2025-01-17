# This script turns on and shows the drone camera
import cv2
from djitellopy import tello
from time import sleep
import threading



def show_camera_frames(drone):
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    drone.end()


def movement(drone):
    drone.move_forward(100)
    sleep(5)
    drone.land()

def main():
    # Initialize drone
    drone = tello.Tello()
    # Connect to drone
    drone.connect()
    # Turn on drone cam
    drone.takeoff()
    drone.streamon()
    # Call the cv camera function
    show_camera_frames(drone)

    t1 = threading.Thread(target=movement, args=(drone))
    t2 = threading.Thread(target=show_camera_frames, args=(drone))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()