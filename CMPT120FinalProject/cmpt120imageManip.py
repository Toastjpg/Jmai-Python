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
    Inverts the color of an image by modifying the RGB values
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    for column in array:
        for pixel in column:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return array


def flipHorizontal(array):
    """
    Flips an image along it's horizontal axis by reversing the order of columns
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    flippedArray = []

    for column in array[::-1]:
        flippedArray.append(column)
    return flippedArray


def flipVertical(array):
    """
    Flips an image along it's vertical axis by reversing the order of pixels in each column
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    for i in range(len(array)):
        array[i] = array[i][::-1]
    return array


# Intermediate functions
def removeRed(array):
    """
    Sets R values of all pixels in the image to 0
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    for column in array:
        for pixel in column:
            pixel[0] = 0
    return array


def removeGreen(array):
    """
    Sets G values of all pixels in the image to 0
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    for column in array:
        for pixel in column:
            pixel[1] = 0
    return array


def removeBlue(array):
    """
    Sets B values of all pixels in the image to 0
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    for column in array:
        for pixel in column:
            pixel[2] = 0
    return array


def greyscale(array):
    """
    Sets all RGB values pixels to a shade of grey
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
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
    Returns: 2D array of RGB values
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
    Decreases the brightness of each pixel. Removes 10 from each of the R/G/B values.
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
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
    Increases the brightness of each pixel. Adds 10 to each of the R/G/B values.
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
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
    """
    Rotates the image 90 degrees to the left.
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    # Create a black image with a width equal to the height of array and a height equal to the width of array
    tempArray = cmpt120imageProj.createBlackImage(len(array[0]), len(array))

    # Iterate over the dimensions of tempArray and grab RGB values from original array
    for i in range(len(tempArray)):
        for j in range(len(tempArray[i])):
            tempArray[i][-j] = array[j][i]
    return tempArray


def rotateRight(array):
    """
    Rotates the image 90 degrees to the left.
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    # Create a black image with a width equal to the height of array and a height equal to the width of array
    tempArray = cmpt120imageProj.createBlackImage(len(array[0]), len(array))

    # Iterate over the dimensions of tempArray and grab RGB values from original array
    for i in range(len(tempArray)):
        for j in range(len(tempArray[i])):
            tempArray[-i][j] = array[j][i]
    return tempArray


def pixelate(array):
    """
    Reduces the quality of an image by averaging the R/G/B values of pixels in 4x4 blocks.
    Input: array - takes in 2D array of RGB values
    Returns: 2D array of RGB values
    """
    # Iterate over image in blocks of 4x4 pixel
    for x in range(0, len(array), 4):
        for y in range(0, len(array[x]), 4):
            red = 0
            green = 0
            blue = 0
            # Accumulate RGB values for all pixels within a 4x4 block
            for column in array[x:x+4]:
                for pixel in column[y:y+4]:
                    red += pixel[0]
                    green += pixel[1]
                    blue += pixel[2]
            # Set pixels in the 4x4 block to the averaged RGB value
            for column in array[x:x+4]:
                for pixel in column[y:y+4]:
                    pixel[0] = red/16
                    pixel[1] = green/16
                    pixel[2] = blue/16
    return array


def binarize(array):
    """
    Creates a black and white image based on calculated threshold values
    Input: array - takes in 2D array of RGB values
    Output: 2D array of RBG values
    """
    count = 0
    bgCount = 0
    fgCount = 0

    # Convert tempArray to greyscale
    for column in array:
        for pixel in column:
            average = (pixel[0] + pixel[1] + pixel[2]) / 3
            pixel[0] = average
            pixel[1] = average
            pixel[2] = average
            count += pixel[0]

    # Calculate the average threshold
    threshold = count/(len(array) * len(array[0]))

    # Separates pixels from array into background or foreground based on threshold
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j][0] <= threshold or array[i][j][1] <= threshold or array[i][j][2] <= threshold:
                bgCount += array[i][j][0]
            else:
                fgCount += array[i][j][0]

    average = ((bgCount/(len(array) * len(array[0]))) + (fgCount/(len(array) * len(array[0]))))/2

    # Check if the difference between threshold and average is greater than 10
    if abs(threshold - average) > 10:
        cont = True
        # Loop through and calculate a new average
        while cont:
            threshold = average
            bgCount = 0
            fgCount = 0
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if array[i][j][0] <= threshold or array[i][j][1] <= threshold or array[i][j][2] <= threshold:
                        bgCount += array[i][j][0]
                    else:
                        fgCount += array[i][j][0]

            average = ((bgCount / (len(array) * len(array[0]))) + (fgCount / (len(array) * len(array[0])))) / 2
            # Check the difference between new average and old average, otherwise continue
            if abs(threshold - average) <= 10:
                threshold = average
                cont = False

    # Iterate over pixels of greyscaled image and set to 0 or 255 if less than or greater than threshold
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j][0] <= threshold:
                array[i][j][0] = 0
                array[i][j][1] = 0
                array[i][j][2] = 0
            else:
                array[i][j][0] = 255
                array[i][j][1] = 255
                array[i][j][2] = 255

    return array
