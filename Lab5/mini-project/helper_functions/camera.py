from picamera2 import Picamera2, Preview
from libcamera import Transform
from time import sleep
import os
from PIL import Image

# returns camera instance
def get_camera():
    picam2 = Picamera2()
    return picam2

# Takes in camera instance and preview time
# displays camera preview for the indicated amount of time
def camera_preview(camera, preveiw_time):
    prev_config = camera.create_preview_configuration()
    camera.configure(prev_config)
    camera.start_preview(Preview.QT)
    sleep(preveiw_time)
    camera.stop_preview()

# Takes in camera instance and degrees
# rotates camera to the indicated degree
def rotate_camera(camera,degrees):
    if degrees == 180:
        pic_config = camera.create_still_configuration(Preview.QT, transform=Transform(hflip=1,vflip=1))
        camera.configure(pic_config)
        camera.start_preview(Preview.QT)
        sleep(2)
        camera.stop_preview()
        camera.start()

# Takes in camera instance, output image location, countdown time and preview Boolean
# If preview is true, preview is started
# The code waits the indicated countdown time before the image is taken and stored in the indicated location
# the preview is stopped if it was started
def capture_image(camera,image_out_location, countdown_time = 0, preview = False ):
    pic_config = camera.create_still_configuration()
    camera.configure(pic_config)

    if preview == True:
        camera.start_preview(Preview.QT)
        sleep(countdown_time)
        camera.stop_preview()
        camera.start()
        sleep(1)
        captured_image = camera.capture_file("pic.jpg")

        # Extract the directory part from location input
        target_directory = os.path.dirname(image_out_location)

        # Create the target directory if it doesn't exist
        os.makedirs(target_directory, exist_ok=True)

        image = Image.open("pic.jpg")

        # save captured image to the file
        image.save(image_out_location)

        # Close camera once finished with it
        camera.stop()
        camera.stop_preview()

    else:
        sleep(countdown_time)

        camera.start()
        sleep(1)
        captured_image = camera.capture_file("pic.jpg")

        # Extract the directory part from location input
        target_directory = os.path.dirname(image_out_location)

        # Create the target directory if it doesn't exist
        os.makedirs(target_directory, exist_ok=True)

        image = Image.open("pic.jpg")

        # save captured image to the file
        image.save(image_out_location)

        # Close camera once finished with it
        camera.stop()
        camera.stop_preview()


# Takes in camera instance, output video location, video length, countdown time and preview Boolean
# If preview is true, preview is started
# The code waits the indicated countdown time before the video is taken for the indicated amount of time 
# and stored in the indicated location
# the preview is stopped if it was started
def capture_video(camera,video_out_location, video_length, countdown_time = 0, preview = False):

    if preview == True:
        camera.start_preview(Preview.QT)
        sleep(countdown_time)
        camera.stop_preview()

        # Record video
        captured_video = camera.start_and_record_video("vid.mp4", duration=video_length)

        # Extract the directory part from location input
        target_directory = os.path.dirname(video_out_location)

        # Create the target directory if it doesn't exist
        os.makedirs(target_directory, exist_ok=True)

        # save captured video to the file
        with open(video_out_location, 'w') as file:
            file.write(captured_video)

        camera.stop()
        camera.stop_preview()

    else:
        sleep(countdown_time)

        # Record video
        captured_video = camera.start_and_record_video("vid.mp4", duration=video_length)

        # Extract the directory part from location input
        target_directory = os.path.dirname(video_out_location)

        # Create the target directory if it doesn't exist
        os.makedirs(target_directory, exist_ok=True)

        # save captured image to the file
        with open(video_out_location, 'w') as file:
            file.write(captured_video)

        camera.stop()
        camera.stop_preview()