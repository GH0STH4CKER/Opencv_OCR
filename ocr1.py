from cv2 import cv2
import pytesseract

img = cv2.imread('C:\\Users\\Dimuth De Zoysa\\Desktop\\ocrsample.png')

text = pytesseract.image_to_string(img)

print(text)