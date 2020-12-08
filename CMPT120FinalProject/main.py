# CMPT 120 Yet Another Image Processor
# Starter code for main.py
# Author(s): Johnny Mai
# Date: December 4th, 2020
# Description: An image processor

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
                "1: Switch to Advanced Functions",
                "2: Switch to Intermediate Functions",
                "3: Invert Image",
                "4: Flip Horizontal",
                "5: Flip Vertical"
         ]

# list of intermediate operation options
intermediate = [
                "1: Switch to Basic Functions",
                "2: Switch to Advanced Functions",
                "3: Remove Red Channel",
                "4: Remove Green Channel",
                "5: Remove Blue Channel",
                "6: Convert to Greyscale",
                "7: Apply Sepia Filter",
                "8: Decrease Brightness",
                "9: Increase Brightness"
                 ]

# list of advanced operation options
advanced = [
                "1: Switch to Intermediate Functions",
                "2: Switch to Basic Functions",
                "3: Rotate Left",
                "4: Rotate Right",
                "5: Pixelate Image",
                "6: Binarize Image"
             ]


# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-5)...")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-9)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-4)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString


# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "O":
            print("Log: Opening Image...")
            state["lastUserInput"] = "O"
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            # Check if a file is actually selected by the user
            if openFilename:
                state["lastOpenFilename"] = openFilename
                img = cmpt120imageProj.getImage(openFilename)
                # call the cmpt120imageProj.getImage with openFilename to get the pixels
            else:
                pass
        elif userInput == "S":
            print("Log: Saving Image...")
            state["lastUserInput"] = "S"
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            if saveFilename:
                state["lastSaveFilename"] = saveFilename
                cmpt120imageProj.saveImage(img, saveFilename)
                img = cmpt120imageProj.getImage(saveFilename)
                # call the cmpt120imageProj.saveImage with saveFilename to save the pixels
            else:
                pass
        elif userInput == "R":
            print("Log: Reloading Original Image...")
            state["lastUserInput"] = "R"
            img = cmpt120imageProj.getImage(state["lastOpenFilename"])
        else:
            print("Log: Unrecognized user input: " + userInput)

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        if state["mode"] == "basic":
            if userInput == "1":
                state["mode"] = "advanced"
                state["lastUserInput"] = "1"
            elif userInput == "2":
                state["mode"] = "intermediate"
                state["lastUserInput"] = "2"
            elif userInput == "3":
                state["lastUserInput"] = "3"
                img = cmpt120imageManip.invert(img)
            elif userInput == "4":
                state["lastUserInput"] = "4"
                img = cmpt120imageManip.flipHorizontal(img)
            elif userInput == "5":
                state["lastUserInput"] = "5"
                img = cmpt120imageManip.flipVertical(img)
            else:
                print("Log: Unrecognized user input: " + userInput)

        elif state["mode"] == "intermediate":
            if userInput == "1":
                state["mode"] = "basic"
                state["lastUserInput"] = "1"
            elif userInput == "2":
                state["mode"] = "advanced"
                state["lastUserInput"] = "2"
            elif userInput == "3":
                state["lastUserInput"] = "3"
                img = cmpt120imageManip.removeRed(img)
            elif userInput == "4":
                state["lastUserInput"] = "4"
                img = cmpt120imageManip.removeBlue(img)
            elif userInput == "5":
                state["lastUserInput"] = "5"
                img = cmpt120imageManip.removeGreen(img)
            elif userInput == "6":
                state["lastUserInput"] = "6"
                img = cmpt120imageManip.greyscale(img)
            elif userInput == "7":
                state["lastUserInput"] = "7"
                img = cmpt120imageManip.applySepia(img)
            elif userInput == "8":
                state["lastUserInput"] = "8"
                img = cmpt120imageManip.decBrightness(img)
            elif userInput == "9":
                state["lastUserInput"] = "9"
                img = cmpt120imageManip.incBrightness(img)
            else:
                print("Log: Unrecognized user input: " + userInput)

        elif state["mode"] == "advanced":
            if userInput == "1":
                state["mode"] = "intermediate"
                state["lastUserInput"] = "1"
            elif userInput == "2":
                state["mode"] = "basic"
                state["lastUserInput"] = "2"
            elif userInput == "3":
                state["lastUserInput"] = "3"
                img = cmpt120imageManip.rotateLeft(img)
            elif userInput == "4":
                state["lastUserInput"] = "4"
                img = cmpt120imageManip.rotateRight(img)
            elif userInput == "5":
                state["lastUserInput"] = "5"
                img = cmpt120imageManip.pixelate(img)
            elif userInput == "6":
                state["lastUserInput"] = "6"
                img = cmpt120imageManip.binarize(img)
            else:
                print("Log: Unrecognized user input: " + userInput)
        else:
            print("Log: Unrecognized mode...")

    else:  # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)

    return img


# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                print("Log: Quitting...")
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
                # Update interface to show currentImg and menu after each user input
                cmpt120imageProj.showInterface(currentImg, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
        elif event.type == pygame.QUIT:  # another way to quit the program is to click the close button
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")