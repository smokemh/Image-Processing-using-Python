import cv2 as cv
import numpy as np

img = cv.imread("OpenCV Basics/Photos/dota2.jpg")
cv.imshow("dota2", img)


#############################
#        Translation        #
#############################


# defining a function to translate an image
def translate(img, x, y):
    transMat = np.float32(
        [[1, 0, x], [0, 1, y]]
    )  # 1 is the x-axis, 0 is the y-axis and x and y are the number of pixels to move
    dimensions = (
        img.shape[1],
        img.shape[0],
    )  # img.shape[1] is the width and img.shape[0] is the height
    return cv.warpAffine(img, transMat, dimensions)


## negative x moves the image to the left and positive x moves the image to the right
## negative y moves the image up and positive y moves the image down

Translated = translate(img, 50, 50)
cv.imshow("Translated", Translated)

## lets now shift the image to the left and up
Translated2 = translate(img, -50, -50)
cv.imshow("Translated2", Translated2)


#############################
#        Rotation           #
#############################


def rotate(img, angle, rotationP=None):
    (height, width) = img.shape[:2]

    if rotationP is None:
        rotationP = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotationP, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


Rotation = rotate(img, 90)
cv.imshow("Rotation", Rotation)

# for a 90 degree rotation we can also use the transpose function as shown below:
Rotation2 = cv.transpose(img)
cv.imshow("Rotation2", Rotation2)


#############################
#        Flipping          #
#############################

flip = cv.flip(img, -1)  # -1 is both horizontal and vertical
cv.imshow("Flip", flip)
# 0 is vertical flip
# 1 is horizontal flip
# -1 is both horizontal and vertical flip
# we can also use the transpose function to flip the image as shown below:
flip2 = cv.transpose(img)
cv.imshow("Flip2", flip2)


cv.waitKey(0)
