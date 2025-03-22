import cv2
import numpy as np

def detect_potholes(image):
    """Detect potholes in an image using OpenCV."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    #edges = cv2.Canny(gray, 50,100)

    laplacian = cv2.Laplacian(thresh, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    contours, _ = cv2.findContours(laplacian, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt,True)

        if area > 500 and perimeter > 100: 
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
            #x, y, w, h = cv2.boundingRect(cnt)
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    return image
