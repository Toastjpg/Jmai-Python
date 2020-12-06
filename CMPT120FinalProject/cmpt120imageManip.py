# CMPT 120 Yet Another Image Processor
# Starter code for cmpt120imageManip.py
# Author(s): Johnny Mai
# Date: December 5th, 2020
# Description: Image manipulation functions

import cmpt120imageProj
import numpy


# Basic functions
def invert(array):
    """
    Inverts the color of an image
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return array


def flipHorizontal(array):
    """
    Flips an image along it's horizontal axis
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    flippedArray = []

    for column in array[::-1]:
        flippedArray.append(column)
    return flippedArray


def flipVertical(array):
    """
    Flips an image along it's vertical axis
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for i in range(len(array)):
        tempArray = array[i]
        array[i] = tempArray[::-1]
    return array


# Intermediate functions
def removeRed(array):
    """
    Sets R values of all pixels in the image to 0
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            pixel[0] = 0
    return array


def removeGreen(array):
    """
    Sets G values of all pixels in the image to 0
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            pixel[1] = 0
    return array


def removeBlue(array):
    """
    Sets B values of all pixels in the image to 0
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            pixel[2] = 0
    return array


def greyscale(array):
    """
    Sets all RGB values pixels to a shade of grey
    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array of modified RGB values
    """
    for column in array:
        for pixel in column:
            average = (pixel[0] + pixel[1] + pixel[2])/3
            pixel[0] = average
            pixel[1] = average
            pixel[2] = average
    return array


def applySepia(array):
    """
    Applies sepia filter to the image using the formula based on original R/G/B values:
    SepiaRed = (Red * .393) + (Green *.769) + (Blue * .189)
    SepiaGreen = (Red * .349) + (Green *.686) + (Blue * .168)
    SepiaBlue = (Red * .272) + (Green *.534) + (Blue * .131)

    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            SepiaRed = (pixel[0] * .393) + (pixel[1] * .769) + (pixel[2] * .189)
            if SepiaRed > 255:
                SepiaRed = 255
            SepiaGreen = (pixel[0] * .349) + (pixel[1] * .686) + (pixel[2] * .168)
            if SepiaGreen > 255:
                SepiaGreen = 255
            SepiaBlue = (pixel[0] * .272) + (pixel[1] * .534) + (pixel[2] * .131)
            if SepiaBlue > 255:
                SepiaBlue = 255
            pixel[0] = SepiaRed
            pixel[1] = SepiaGreen
            pixel[2] = SepiaBlue
    return array


def decBrightness(array):
    """
    Decreases the brightness of each pixel. Reduces R/G/B value by 10 each time.

    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            if (pixel[0] - 10) < 0:
                pixel[0] = 0
            else:
                pixel[0] -= 10
            if (pixel[1] - 10) < 0:
                pixel[1] = 0
            else:
                pixel[1] -= 10
            if (pixel[2] - 10) < 0:
                pixel[2] = 0
            else:
                pixel[2] -= 10
    return array


def incBrightness(array):
    """
    Decreases the brightness of each pixel. Reduces R/G/B value by 10 each time.

    Input: array - takes in 2D array of RGB values
    Returns: Returns a 2D array with modified RGB values
    """
    for column in array:
        for pixel in column:
            if (pixel[0] + 10) > 255:
                pixel[0] = 255
            else:
                pixel[0] += 10
            if (pixel[1] + 10) > 255:
                pixel[1] = 255
            else:
                pixel[1] += 10
            if (pixel[2] + 10) > 255:
                pixel[2] = 255
            else:
                pixel[2] += 10
    return array


# Advanced Functions
def rotateLeft(array):
    pass


def rotateRight(array):
    pass


def pixelate(array):
    pass


def binarize(array):
    pass
