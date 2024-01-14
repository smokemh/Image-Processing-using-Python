import cv2 as cv

img = cv.imread("OpenCV Basics/Photos/dota2.jpg")


###########################
#    Read in an image     #
###########################
cv.imshow("dota2", img)

###########################
# Converting to grayscale #
###########################

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

###########################
#         BLUR            #
###########################

## Gaussian Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)  # 7,7 is the kernel size
cv.imshow("Gaussian Blur", blur)


## Average Blurring (Normalized Box Filter):
blur2 = cv.blur(img, (5, 5))  # 5,5 is the kernel size
cv.imshow("Average Blur", blur2)

## Median Blur
median = cv.medianBlur(img, 5)  # 5 is the kernel size
cv.imshow("Median Blur", median)


## Bilateral Blur
bilateral = cv.bilateralFilter(
    img, 10, 35, 25
)  # 10 is the diameter, 35 is the sigma color, 25 is the sigma space
cv.imshow("Bilateral Blur", bilateral)


###########################
#       Edge Cascade      #
###########################

## Canny Edge Cascade
canny = cv.Canny(img, 125, 175)  # 125 is the threshold 1, 175 is the threshold 2
cv.imshow("Canny Edges", canny)

### To reduce the amount of edges found we can simply pass in a blurred image instead of the original image to the Canny function as shown below:
canny2 = cv.Canny(blur, 125, 175)  # 125 is the threshold 1, 175 is the threshold 2
cv.imshow("Canny Edges with Blur", canny2)

## Sobel Edge Cascade
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)  # x # cv.CV_64F is the depth
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)  # y # ksize is the kernel size
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)

## Laplacian Edge Detection
laplacian = cv.Laplacian(img, cv.CV_64F)  # cv.CV_64F is the depth
cv.imshow("Laplacian", laplacian)

## Scharr Operator
scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
scharry = cv.Scharr(img, cv.CV_64F, 0, 1)
cv.imshow("Scharr X", scharrx)
cv.imshow("Scharr Y", scharry)

###########################
#    Dilating the image   #
###########################

### Use the canny image to dilate the edges
dilated = cv.dilate(canny, (8, 8), iterations=2)  # 8,8 is the kernel size
cv.imshow("Dilated", dilated)


###########################
#         Eroding         #
###########################

## Use the dilated image to erode the edges back to the original image
eroded = cv.erode(dilated, (8, 8), iterations=2)  # 8,8 is the kernel size
cv.imshow("Eroded", eroded)

###########################
#         Resize          #
###########################
resize = cv.resize(
    img, (500, 500)
)  # (500,500) is the new size of the image ignoring the aspect ratio
cv.imshow("Resized", resize)

### we can also resize the image by interpolating the pixels
resize2 = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized2", resize2)

###########################
#        Cropping         #
###########################

### since images are arrays and we can slice them like arrays to crop them
cropped = img[50:200, 200:400]  # [height,width]
cv.imshow("Cropped", cropped)

# lets try to get logo of dota 2
cropped2 = img[278:350, 318:412]  # [height,width]
cv.imshow("Dota2 Logo", cropped2)
cv.waitKey(0)
