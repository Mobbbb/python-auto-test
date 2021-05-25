import base64

import cv2
import numpy as np
from skimage.measure import compare_ssim, compare_mse


def ssim_sim(image, image_baseline):
    # load the two input images
    # imageA = cv2.imread(image_a)
    # imageB = cv2.imread(image_b)

    if image is not None and image_baseline is not None:
        baseline_size = cv_size(image_baseline)
        image = cv2.resize(image, baseline_size)
        grayA = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(image_baseline, cv2.COLOR_BGR2GRAY)
        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        print('mse', compare_mse(grayA, grayB))
        (score, diff) = compare_ssim(grayA, grayB, full=True, gaussian_weights=True, use_sample_covariance=False)
        # diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))
        return score
    else:
        return 0


def cv_size(img):
    return tuple(img.shape[1::-1])


def read_base64(uri):
    encoded_data = uri
    if ',' in encoded_data:
        encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def image_diff_base64(image, image_baseline, method='sift'):
    if image and image_baseline:
        if method is 'sift':
            return sift_sim(read_base64(image), read_base64(image_baseline), False)
        else:
            return ssim_sim(read_base64(image), read_base64(image_baseline))
    return 0


def sift_sim(image, image_baseline, is_gray=True):
    """
    Use SIFT features to measure image similarity
    """
    # check valid
    if image is None or image_baseline is None:
        return 0

    # initialize the sift feature detector
    orb = cv2.ORB_create()

    # convert to gray
    if not is_gray:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_baseline = cv2.cvtColor(image_baseline, cv2.COLOR_BGR2GRAY)

    # detect
    kp_a, desc_a = orb.detectAndCompute(image, None)
    kp_b, desc_b = orb.detectAndCompute(image_baseline, None)

    # BFMatcher with default params
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # match.distance is a float between {0:100} - lower means more similar
    matches = bf.match(desc_a, desc_b)

    similar_regions = [i for i in matches if i.distance < 40]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)
