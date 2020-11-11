import cmpt120imageWeek9


def invert(array):
    # Iterate over each column in 2d array
    for column in array:
        # Iterate over each pixel in the column
        for pixel in column:
            # Invert RGB values of each pixel
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return array


def cover(array):
    # Check if the height of image is even or odd.
    if len(array[0]) % 2 != 0:
        midPoint = (len(array[0])//2) + 1
    else:
        midPoint = (len(array[0])//2)
    # Iterate over each column in 2d array
    for column in array:
        # Iterate over each pixel in the column from midPoint to bottom
        for pixel in column[midPoint:]:
            # Edit each RGB value to black
            pixel[0] = 0
            pixel[1] = 0
            pixel[2] = 0
    return array


def flip_horizontal(array):
    flippedArray = []

    # Iterate over each column number in 2d array backwards
    for column in array[::-1]:
        # Add each column to the a new array in the backwards order
        flippedArray.append(column)
    return flippedArray



