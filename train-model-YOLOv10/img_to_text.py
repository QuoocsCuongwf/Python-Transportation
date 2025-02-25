import cv2
import pytesseract

# Đường dẫn đến tệp thực thi Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Đọc hình ảnh
image_path = f'D:\\code\\python-transportation\\train-model-YOLOv10\\plate.png'
img = cv2.imread(image_path)

# Chuyển đổi hình ảnh sang văn bản
text = pytesseract.image_to_string(img)

# In văn bản đã chuyển đổi
print('text: ',text)