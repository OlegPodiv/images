import cv2
import pytesseract
from imutils import contours

image = cv2.imread("Deblur.png")

height, width, _ = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = contours.sort_contours(cnts[1])

for c in cnts:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    if area > 5000:
        img = image[y:y+h, x:x+w]
        result = pytesseract.image_to_string(img, lang="eng")
        if len(result) > 7:
            print(result)
# print(cnts)
cv2.imshow("Test", thresh)
cv2.waitKey()
