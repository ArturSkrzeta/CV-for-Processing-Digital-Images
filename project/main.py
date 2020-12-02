import cv2
import pytesseract

TESSERACT_DIR = r"C:\Tesseract-OCR\tesseract.exe"

def main():

    pytesseract.pytesseract.tesseract_cmd = TESSERACT_DIR

    # reading image in
    img = cv2.imread('page.jpg')
    # resizing image
    img = cv2.resize(img, None, fx=0.6, fy=0.6)
    # plaining image
    grayed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive_threshold = cv2.adaptiveThreshold(grayed_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 11)
    # convering image to txt
    text = pytesseract.image_to_string(adaptive_threshold, config="--psm 3")
    # printing text
    print(text)
    # showing plain image
    # cv2.imshow('image', adaptive_threshold)
    # cv2.waitKey(0)

if __name__ == '__main__':
    main()
