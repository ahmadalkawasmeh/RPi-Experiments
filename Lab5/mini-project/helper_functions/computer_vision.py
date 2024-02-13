from PIL import Image
import numpy as np


# Takes in image1 and image2 locations and t1
# returns a Boolean indicating if a "person” is in the image based on t1
def person_detected(image1_file, image2_file, t1):
    color_image1 = Image.open(image1_file)
    color_image2 = Image.open(image2_file)

    # Convert to black and white
    bw_image1 = color_image1.convert('L')
    bw_image2 = color_image2.convert('L')

    # Convert to numpy array
    array1 = np.array(bw_image1)
    array2 = np.array(bw_image2)

    # Sum each array
    array1_sum = np.sum(array1)
    array2_sum = np.sum(array2)

    image_difference = np.abs(array1_sum - array2_sum)

    if image_difference >= t1:
        return True

    else:
        return False
