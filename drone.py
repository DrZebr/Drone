from djitellopy import tello
from time import sleep
import cv2
from djitellopy import tello


def show_camera_frames(drone):
    # Shows the camera frames through cv2
    while True:
        frame = drone.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def main():
    # Initialize drone
    drone = tello.Tello()
    # Connect to drone
    drone.connect()
    # Turn on drone cam
    drone.streamon()
    # Call the cv camera function
    show_camera_frames(drone)
    sleep(1)
    # connects
    drone.query_battery()
    # gets the battery percent
    sleep(1)
    drone.takeoff()
    sleep(4)
    # Takes off
    drone.rotate_counter_clockwise(90)
    sleep(6)
    drone.rotate_clockwise(90)
    sleep(6)
    # rotates back and forth
    drone.land()
    # lands
    drone.end()


if __name__ == "__main__":
    main()
