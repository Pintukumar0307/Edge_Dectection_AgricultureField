import numpy as np
import os
import cv2
# import matplotlib.pyplot as plt



def Canny_detector(img, weak_th=None, strong_th=None):
    """
    Applies Canny edge detection to the input image.

    Args:
    - img: Input image.
    - weak_th: Weak threshold for double thresholding step.
    - strong_th: Strong threshold for double thresholding step.

    Returns:
    - mag: Magnitude of gradients of edges.
    """
    # Conversion of image to grayscale
    if len(img.shape) == 3:  # Ensure input image is grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction step
    img = cv2.GaussianBlur(img, (5, 5), 1.4)

    # Calculating the gradients
    gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)

    # Conversion of Cartesian coordinates to polar
    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)

    # Setting default thresholds if not provided
    mag_max = np.max(mag)
    if weak_th is None:
        weak_th = mag_max * 0.05
    if strong_th is None:
        strong_th = mag_max * 0.5

    # Double thresholding step
    weak_ids = mag < weak_th
    strong_ids = mag > strong_th
    ids = np.zeros_like(img)
    ids[strong_ids] = 255  # Strong edges
    ids[np.logical_and(mag <= strong_th, mag >= weak_th)] = 50  # Weak edges

    # Non-maximum suppression step
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            if ids[i, j] == 50:  # Weak edge
                if np.any(ids[i - 1:i + 2, j - 1:j + 2] == 255):
                    ids[i, j] = 255

    return ids

def Canny_detector1(img, weak_th=None, strong_th=None):
    """
    Applies Canny edge detection to the input image.

    Args:
    - img: Input image.
    - weak_th: Weak threshold for double thresholding step.
    - strong_th: Strong threshold for double thresholding step.

    Returns:
    - mag: Magnitude of gradients of edges.
    """
    # Conversion of image to grayscale
    if len(img.shape) == 3:  # Ensure input image is grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction step
    img = cv2.GaussianBlur(img, (5, 5), 1.4)

    # Calculating the gradients
    gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)

    # Conversion of Cartesian coordinates to polar
    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)

    # Setting default thresholds if not provided
    mag_max = np.max(mag)
    if weak_th is None:
        weak_th = mag_max * 0.05
    if strong_th is None:
        strong_th = mag_max * 0.5

    # Double thresholding step
    weak_ids = mag < weak_th
    strong_ids = mag > strong_th
    ids = np.zeros_like(img)
    ids[strong_ids] = 255  # Strong edges
    ids[np.logical_and(mag <= strong_th, mag >= weak_th)] = 50  # Weak edges

    # Non-maximum suppression step
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            if ids[i, j] == 50:  # Weak edge
                if np.any(ids[i - 1:i + 2, j - 1:j + 2] == 255):
                    ids[i, j] = 255

    return ids


def calculate_area(contours):
    """
    Calculate the area of the largest contour.

    Args:
    - contours: List of contours detected in the image.

    Returns:
    - area: Area of the largest contour.
    """
    if len(contours) == 0:
        return 0
    max_contour = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(max_contour)
    return area


def calculate_image_area(img):
    """
    Calculates the area of the input image.

    Args:
    - img: Input image.

    Returns:
    - area: Area of the input image.
    """
    # Get the dimensions of the image
    height, width = img.shape[:2]

    # Calculate the area by multiplying width and height
    area = width * height

    return area

def find_edge_area(edge_img):
    """
    Finds the area of edges in the given edge image.

    Args:
    - edge_img: Image containing detected edges.

    Returns:
    - area: Area of detected edges.
    """
    # Counting non-zero pixels (edges)
    area = np.count_nonzero(edge_img)
    return area

def find_non_detected_edge_area(edge_img):
    """
    Finds the area of non-detected edges (background) in the given edge image.

    Args:
    - edge_img: Image containing detected edges.

    Returns:
    - area: Area of non-detected edges (background).
    """
    # Total area of the image
    total_area = edge_img.shape[0] * edge_img.shape[1]

    # Area of detected edges
    edge_area = np.count_nonzero(edge_img)

    # Area of non-detected edges (background)
    non_detected_edge_area = total_area - edge_area

    return non_detected_edge_area

def calculate_percentage_detected_edge(edge_img):
    """
    Calculates the percentage of detected edges in the input edge image.

    Args:
    - edge_img: Image containing detected edges.

    Returns:
    - percentage: Percentage of detected edges.
    """
    # Calculate the area of detected edges
    detected_edge_area = np.count_nonzero(edge_img)

    # Calculate the total area of the image
    total_area = edge_img.shape[0] * edge_img.shape[1]

    # Calculate the percentage of detected edges
    percentage_detected_edge = (detected_edge_area / total_area) * 100

    return percentage_detected_edge

def calculate_percentage_non_detected_edge(edge_img):
    """
    Calculates the percentage of non-detected edges (background) in the input edge image.

    Args:
    - edge_img: Image containing detected edges.

    Returns:
    - percentage: Percentage of non-detected edges (background).
    """
    # Calculate the area of non-detected edges (background)
    non_detected_edge_area = find_non_detected_edge_area(edge_img)

    # Calculate the total area of the image
    total_area = edge_img.shape[0] * edge_img.shape[1]

    # Calculate the percentage of non-detected edges (background)
    percentage_non_detected_edge = (non_detected_edge_area / total_area) * 100

    return percentage_non_detected_edge

