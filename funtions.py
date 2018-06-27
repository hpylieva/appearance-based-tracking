import sys
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def plot_match_result(img, match_result, top_left, bottom_right, method_name):
    """
    Plot results of template matching.
    Images are automatically scaled in plt.imshow() like:
    img = (img - np.min(img))/(np.max(img) - np.min(img))
    :param img:
    :param match_result:
    :param top_left:
    :param bottom_right:
    :param method_name:
    :return:
    """
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(match_result,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(method_name)
    plt.show()

def template_matching(image, template, method = 'SSD'):
    """
    Computes template matching.
    :param image: image in the grey scale
    :param templ: template in grey scale
    :param method: chosen appearance similarity function for convolution
    :return: Result of comparison the template to cutted aread from image in each point.
    The minimum pr maximum value of this result will be loaction of top left corner of image we search
    """
    im_height, im_width = image.shape
    t_height, t_width = template.shape

    res = np.zeros((im_height - t_height, im_width - t_width))
    image = np.array(image, dtype = 'float32')
    # loop through the search image
    for h in range(im_height - t_height):
        for w in range(im_width - t_width):
            patch = image[h:(h+t_height), w:(w+t_width)]
            if method=='SSD':
                res[h, w] = np.sum(np.power(patch - template,2))
            elif method=='NCC':
                res[h, w] = np.sum(np.multiply(patch, template))
                # np.sum(np.multiply(image[w:(w+t_height), h:(h+t_width)], templ))
                res[h, w] /= np.sqrt(np.sum(np.square(patch)) * np.sum(np.square(template)))
            elif method=='SAD':
                res[h, w] = np.sum(np.absolute(patch- template))
    return res


def LK(image):
    pass
