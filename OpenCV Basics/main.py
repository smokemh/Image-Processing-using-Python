import cv2 as cv


##Resize Function
def rescalFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # Width of the image
    height = int(frame.shape[0] * scale)  # Height of the image
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def changeRes(width, height):  # Function for changing resoltuion of live video
    capture.set(3, width)
    capture.set(4, height)


class Importpicture:
    def __init__(self):
        img = cv.imread("OpenCV Basics/Photos/Dlarge.jpg")
        resized_img = rescalFrame(img, 0.5)  # Resizing Image with 50 percent
        cv.imshow("Dota2 large", img)
        cv.imshow("Dots2 Resized", resized_img)
        cv.waitKey(0)


class Importvideo:
    def __init__(self):
        capture = cv.VideoCapture(
            "OpenCV Basics/Videos/video.mp4"
        )  # If given argument of integers that means we are using Webcam like cv.VideoCapture (0) means webcam
        while True:
            isTrue, frame = capture.read()
            resized_vid = rescalFrame(frame, 0.5)  # 50 percent
            cv.imshow("Video", frame)
            cv.imshow("Video Resized", resized_vid)

            if cv.waitKey(20) & 0xFF == ord("d"):
                break
        capture.release()
        cv.destroyAllWindows()


view_picture = Importpicture()
view_video = Importvideo()
