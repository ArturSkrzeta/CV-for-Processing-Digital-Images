import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

img = cv2.imread('page.jpg')
img = cv2.resize(img, None, fx=0.6, fy=0.6)
grayed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(grayed_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 11)
text = pytesseract.image_to_string(adaptive_threshold, config="--psm 3")
print(text)

cv2.imshow('image', adaptive_threshold)
cv2.waitKey(0)
