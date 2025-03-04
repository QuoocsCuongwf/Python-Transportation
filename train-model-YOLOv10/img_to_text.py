import cv2
import pytesseract

# Đường dẫn đến tệp thực thi Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Đọc hình ảnh
image_path = f'D:\\code\\python-transportation\\train-model-YOLOv10\\plate.png'
img = cv2.imread(image_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

theard, blackandwhite = cv2.threshold(img_gray, 255, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# Chuyển đổi hình ảnh sang văn bản
text = pytesseract.image_to_string(blackandwhite, lang='eng')
cv2.imshow('image', img)
cv2.imshow('blackandwhite', blackandwhite)
# In văn bản đã chuyển đổi
print('text: ',text)
cv2.waitKey(0)
cv2.destroyAllWindows()