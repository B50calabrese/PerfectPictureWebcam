# Imports specifically for OpenCV.
import numpy as np
import cv2

# Constants.
DEBUG = True
MODE_FACE_DETECT = 1
MODE_ARROW_CONTROL = 2
HIGHEST_MODE = 2
LOWEST_MODE = 1
MODE_FACE_DETECT_TEXT = "Automatic Positioning"
MODE_ARROW_CONTROL_TEXT = "Manual Positioning"
MODE_TEXT_POSITION = (0, 450)
HIGHLIGHT_TEXT = "Highlighting Faces"
HIGHLIGHT_TEXT_POSITION = (0, 430)
WINDOW_NAME = "Perfect Picture"
DEFAULT_HIGHLIGHT_COLOR = (255, 0, 0)
DEFAULT_FONT_SCALE = .75
DEFAULT_FONT_COLOR = (255, 255, 255)
DEFAULT_FACE_CENTER_COLOR = (0, 0, 255)
DEFAULT_IMG_CENTER_COLOR = (0, 255, 0)
DEFAULT_WINDOW_WIDTH = 640
DEFAULT_WINDOW_HEIGHT = 480
ESCAPE_KEY_CODE = 27
H_KEY_CODE = 104
W_KEY_CODE = 119
A_KEY_CODE = 97
S_KEY_CODE = 115
D_KEY_CODE = 100
M_KEY_CODE = 109

# Global variables.
current_mode = MODE_FACE_DETECT
highlight_faces = True
highlight_rectangle_color = DEFAULT_HIGHLIGHT_COLOR

# Global Objects for OPENCV
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = DEFAULT_FONT_SCALE
font_color = DEFAULT_FONT_COLOR

# Prints the message passed if this is in debug mode.
def printLog(message):
    if DEBUG:
        print message

# Highlights all of the faces in the image.
def highlightFaces(img, faces):
    global highlight_faces
    if not highlight_faces:
        return
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), highlight_rectangle_color, 2)

# Adds the various pieces of status texts to the image.
def addTexts(img):
    global current_mode
    global MODE_FACE_DETECT
    global MODE_FACE_DETECT_TEXT
    global MODE_ARROW_CONTROL
    global MODE_ARROW_CONTROL_TEXT
    global MODE_TEXT_POSITION
    global font
    global DEFAULT_FONT_SCALE
    global highlight_faces
    global HIGHLIGHT_TEXT
    global HIGHLIGHT_TEXT_POSITION
    global DEFAULT_FONT_COLOR

    modeStr = "Current Mode : "
    if current_mode == MODE_FACE_DETECT:
        modeStr = modeStr + MODE_FACE_DETECT_TEXT
    elif current_mode == MODE_ARROW_CONTROL:
        modeStr = modeStr + MODE_ARROW_CONTROL_TEXT
    cv2.putText(img, modeStr, MODE_TEXT_POSITION, font, DEFAULT_FONT_SCALE, DEFAULT_FONT_COLOR, 2, cv2.LINE_AA)


    if highlight_faces:
        cv2.putText(img, HIGHLIGHT_TEXT, HIGHLIGHT_TEXT_POSITION, font, DEFAULT_FONT_SCALE, DEFAULT_FONT_COLOR, 2, cv2.LINE_AA)
    
    return

# Camera movement routines.
def moveCamLeft():
    printLog("Move camera left")

def moveCamRight():
    printLog("Move camera right")

def moveCamUp():
    printLog("Move camera up")

def moveCamDown():
    printLog("Move camera down")

# Handles any user input, specifically returning true when the escape key is pressed.
def handleInputs():
    global highlight_faces
    global current_mode
    global MODE_ARROW_CONTROL
    global HIGHEST_MODE
    global LOWEST_MODE
    
    key = cv2.waitKey(20)

    # If escape key.
    if key == ESCAPE_KEY_CODE:
        return True

    # If h was pressed, change highlighting of faces.
    if key == H_KEY_CODE:
        highlight_faces = not highlight_faces

    # If m was pressed, go to the next mode.
    if key == M_KEY_CODE:
        current_mode = current_mode + 1
        if current_mode > HIGHEST_MODE:
            current_mode = LOWEST_MODE

    if current_mode == MODE_ARROW_CONTROL:
        if key == W_KEY_CODE:
            moveCamUp()

        if key == S_KEY_CODE:
            moveCamDown()

        if key == A_KEY_CODE:
            moveCamLeft()

        if key == D_KEY_CODE:
            moveCamRight()
        
    return False

# Moves the camera based on the center position of the faces.
def faceDetectMove(img, faces):
    global highlight_faces
    global DEFAULT_WINDOW_WIDTH
    global DEFAULT_WINDOW_HEIGHT
    centerX = 0
    centerY = 0
    numFaces = 0
    for (x, y, w, h) in faces:
        numFaces = numFaces + 1
        centerX = centerX + x + (w / 2)
        centerY = centerY + y + (h / 2)

    # If there are no faces, just return.
    if numFaces == 0:
        return
    
    center = (centerX / numFaces, centerY / numFaces)
    centerImg = (DEFAULT_WINDOW_WIDTH / 2, DEFAULT_WINDOW_HEIGHT / 2)

    if (centerImg[0] < center[0]):
        moveCamLeft()
    if (centerImg[0] > center[0]):
        moveCamRight()
    if (centerImg[1] < center[0]):
        moveCamUp()
    if (centerImg[1] > center[0]):
        moveCamDown()

    if highlight_faces:
        cv2.rectangle(img, (center[0] - 2, center[1] - 2), (center[0] + 2, center[1] + 2), DEFAULT_FACE_CENTER_COLOR, 2)
        cv2.rectangle(img, (centerImg[0] - 2, centerImg[1] - 2), (centerImg[0] + 2, centerImg[1] + 2), DEFAULT_IMG_CENTER_COLOR, 2)
    

# Main subroutine that handles the entirety of the logic loop.
def main():
    global MODE_FACE_DETECT
    global current_mode
    
    done = False
    while (not done):
        # Get the actual image capture and list of faces.
        rval, img_from_capture = video_capture.read()
        gray_img = cv2.cvtColor(img_from_capture, cv2.COLOR_BGR2GRAY)
        list_of_faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

        # If we are in face detect mode, then we will move based on the center of the faces and image.
        if current_mode == MODE_FACE_DETECT:
            faceDetectMove(img_from_capture, list_of_faces)

        # Highlights the faces if need be.
        highlightFaces(img_from_capture, list_of_faces)       

        addTexts(img_from_capture)
        cv2.imshow(WINDOW_NAME, img_from_capture)
        cv2.resizeWindow(WINDOW_NAME, DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
        done = handleInputs()

# Start of program.
main()

# Clean up any assets used.
cv2.destroyAllWindows()
video_capture.release()
