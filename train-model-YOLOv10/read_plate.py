import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import easyocr

def read_license_plate(image_path):
    # Tạo đối tượng reader
    reader = easyocr.Reader(['en'])  # Chỉ cần chạy một lần để tải mô hình vào bộ nhớ
    result = reader.readtext(image_path)  # Đọc văn bản từ hình ảnh
    return result
