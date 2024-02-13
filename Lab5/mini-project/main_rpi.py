from helper_functions import camera, computer_vision, sensehat

from time import sleep

def main():
    camera_i = camera.get_camera()  # DO NOT MODIFY, function call must work as is
    sense = sensehat.get_sensehat()  # DO NOT MODIFY, function call must work as is

    # Prompt user for background image choice
    user_background_choice = int(
        input("\n Press '1' if there is a background image already saved, or press '2' to take a new background image "
              "\n"))
    if user_background_choice == 1:
        take_background_image = False
    if user_background_choice == 2:
        take_background_image = True

    # Background capture prompt
    if take_background_image:
        # Countdown image capture of background
        print("\n Please exit the camera view")
        sleep(2)
        print("\n Capturing background image in 10 seconds...\n")
        for n in range(10, 0, -1):
            print(n)
            sleep(1)
        print("\n Background image captured !\n")

        # Capture the actual picture
        preview = False
        countdown = 0
        camera.capture_image(camera_i, "data/images/background.jpg", countdown_time=countdown,
                             preview=preview)  # DO NOT MODIFY, function call must work as is

    # User choice to arm system
    arm_choice = input("Would you like to arm the system? y/n\n")
    if arm_choice == "y":
        arm_system = True  # TO-DO: Should be a user input

    if arm_choice == "n":
        arm_system = False

    if arm_system:
        # Interval prompt
        interval_choice = int(input("Please enter the interval between test images (in seconds): \n"))
        interval = interval_choice

        # Threshold prompt
        threshold_choice = int(input("Please enter the threshold t1 :\n"))
        t1 = threshold_choice

        # t1 = 480000000  # Default threshold

        # Countdown to monitoring
        print("\n Monitoring will begin in 10 seconds ...\n")
        for n in range(10, 0, -1):
            print(n)
            sleep(1)
        print("\nmonitoring has started !\n")

        count = 0
        while True:  # DO NOT MODIFY, function call must work as is
            camera.capture_image(camera_i, "data/images/image%s.jpg" % count,
                                 countdown_time=interval)  # DO NOT MODIFY, function call must work as is
            person_detected = computer_vision.person_detected("data/images/background.jpg",
                                                              "data/images/image%s.jpg" % count,
                                                              t1)  # DO NOT MODIFY, function call must work as is
            if person_detected:  # DO NOT MODIFY, function call must work as is
                print("Person Detected")  # DO NOT MODIFY, function call must work as is
                sensehat.alarm(sense, interval)  # DO NOT MODIFY, function call must work as is
            else:
                print("No Person Detected")  # DO NOT MODIFY, function call must work as is
            count += 1


if __name__ == "__main__":
    main()
