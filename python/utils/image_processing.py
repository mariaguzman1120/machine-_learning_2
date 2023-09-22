import os

import numpy as np
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize


def transform_image(path:str) -> np.array:
    """Convert an image located at 'path_read' to grayscale, resize it to
    (256, 256) pixels, and optionally save it to 'path_save'.

    Args:
        path_read: The path to the input image file.

    Returns:
        np.array: The grayscale image as a NumPy array.

    """
    image = io.imread(path)

    # scaling image
    image = resize(image, (256, 256), anti_aliasing=True)

    # rgb to gray
    image = rgb2gray(image)

    return image


def read_images(path: str) -> list:
    """Read and return a list of images from a specified directory.

    Args:
        path: The path to the directory containing the images.

    Returns:
        A list of image data.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        Exception: If an error occurs while reading an image.

    """
    images_list = os.listdir(path)

    images = []
    for path_image in images_list:
        path_read = os.path.join(path, path_image)
        
        try:
            img = transform_image(path_read)
        except:
            img = io.imread(path_read)
            
        images.append(img)
    
    return images




