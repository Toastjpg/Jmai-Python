import cmpt120imageManip
import cmpt120imageWeek9

while True:
    try:
        loopCont = True
        while loopCont:
            userIn = int(input("What manipulation do you want? (0/1/2/3/4)\n>>> "))

            if userIn == 0:
                loopCont = False

            elif userIn == 1:
                pixels = cmpt120imageWeek9.getImage("week9-photo.jpg")
                cmpt120imageWeek9.showImage(pixels, "Original Image")

            elif userIn == 2:
                invertedArray = cmpt120imageManip.invert(cmpt120imageWeek9.getImage("week9-photo.jpg"))
                cmpt120imageWeek9.showImage(invertedArray, "Inverted Image")

            elif userIn == 3:
                coveredArray = cmpt120imageManip.cover(cmpt120imageWeek9.getImage("week9-photo.jpg"))
                cmpt120imageWeek9.showImage(coveredArray, "Covered Image")

            elif userIn == 4:
                flippedArray = cmpt120imageManip.flip_horizontal(cmpt120imageWeek9.getImage("week9-photo.jpg"))
                cmpt120imageWeek9.showImage(flippedArray, "Flipped Image")

            else:
                print(f"Sorry, I dont understand what {userIn} means.")

    except ValueError:
        print("Sorry, I don't understand what that means.")
