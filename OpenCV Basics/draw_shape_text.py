import cv2 as cv
import numpy as np


data = {
    "hey": 12344,
    "package": {"a": 5, "b": 100, "data": b"123"},
    "True": [1, 2, 3, 4, 5],
    "True": [1, 2, 3, 4, 5],
    "True": [1, 2, 3, 4, 5],
    "True": [1, 2, 3, 4, 5],
    "True": [1, 2, 3, 4, 5],
}

# Getting Blank Image from numpy
blank = np.zeros((500, 500, 3), dtype="uint8")  # 500x500 picture with data type uint8
print(blank.shape[0])

# 1. Paint the image a certain colour
blank[0:100, 400:500] = 255, 0, 0  # Blue , Green , Red
blank[0:100, 0:100] = 255, 0, 0
blank[200:300, 200:300] = 0, 255, 0
blank[400:500, 0:100] = 0, 0, 255
blank[400:500, 400:500] = 0, 0, 255


# 2. Draw a Rectangle
cv.rectangle(
    blank, (100, 100), (250, 250), (0, 255, 0), thickness=1
)  # rectange (img,pt1,pt2,color,thickness,line_type, shift) #for filled use thickness=cv.FILLED
cv.rectangle(blank, (250, 100), (400, 250), (0, 255, 0), thickness=1)
cv.rectangle(blank, (100, 400), (250, 250), (0, 255, 0), thickness=1)
cv.rectangle(blank, (250, 250), (400, 400), (0, 255, 0), thickness=1)
# cv.rectangle(blank,(37,37),(463,463),(0,255,0),thickness=1)

# 3. Draw A circle
cv.circle(
    blank, (250, 250), 213, (0, 255, 0), thickness=1
)  # circle(img, center, radius,color,thickness,line_type, shift)


# 4. Draw a line
cv.line(blank, (100, 100), (400, 400), (0, 255, 0), thickness=3)
cv.line(blank, (100, 400), (400, 100), (0, 255, 0), thickness=3)
cv.line(blank, (0, 0), (100, 100), (0, 0, 255), thickness=3)
cv.line(blank, (500, 500), (400, 400), (255, 0, 0), thickness=3)
cv.line(blank, (500, 0), (400, 100), (0, 0, 255), thickness=3)
cv.line(blank, (100, 400), (0, 500), (255, 0, 0), thickness=3)


# 5. Write text
cv.putText(
    blank, "R=213", (125, 125), cv.FONT_HERSHEY_TRIPLEX, 0.7, (0, 255, 0), 1
)  # putText (img, text, pt1, fontface, fontscae, color, thickness)


cv.imshow("Final Image", blank)

cv.waitKey(0)
