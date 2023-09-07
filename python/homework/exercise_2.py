import matplotlib.pyplot as plt
import numpy as np

from skimage import io
from python.metadata.path import Path
from python.utils.image_processing import read_images
from python.utils.image_processing import transform_image
from python.metadata.responses import Responses

if __name__ == '__main__':

    picture = transform_image(Path.picture)

    plt.imshow(picture, cmap='gray')
    
    io.show()

    plt.close()

    # Calculate and plot the average face of the cohort.
    picture_cohort = read_images(Path.picture_cohort)
    avg_cohort = sum(picture_cohort) / len(picture_cohort)

    plt.imshow(avg_cohort, cmap='gray')
    
    io.show()

    plt.close()

    # How distant is your face from the average? How would you measure it?
    distance = np.linalg.norm(picture - avg_cohort)
    print(distance)
    print(Responses.distance_face)

    
