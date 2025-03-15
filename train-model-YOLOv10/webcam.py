import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import Label
import read_plate
from PIL import Image, ImageTk

# Load the model
model = YOLO(f"D:\\code\\python-transportation\\train-model-YOLOv10\\best.pt")

# Mở webcam (0 là chỉ số của camera đầu tiên)
cap = cv2.VideoCapture(0)
camera_running = False

def start_camera(gui,camera_label,right_frame):
    global cap, camera_running
    camera_running = True
    cap = cv2.VideoCapture(0)  # Sử dụng camera mặc định
    update_frame(gui,camera_label,right_frame)

def stop_camera():
    global camera_running
    camera_running = False
    if cap.isOpened():
        cap.release()  # Dừng camera

def update_frame(gui,camera_label,right_frame):
    if camera_running and cap.isOpened():
        ret, frame = cap.read()  # Đọc một khung hình từ camera
        results = model(frame, stream=True)
        if ret:
            for r in results:
                boxes = r.boxes
                h, w=0,0

                for box in boxes:
                    # bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 1)
                    org = (x1, y1 - 10)  # Vẽ nhãn ngay phía trên hộp bao
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2
                    crop_img = frame[y1:y2, x1:x2]
                    # Hiển thị biển số xe
                    if crop_img.size != 0:
                        cv2.imshow("Crop", crop_img)
                        cv2.imwrite("D:/code/python-transportation/train-model-YOLOv10/crop.jpg", crop_img)
                        result = read_plate.read_license_plate("D:/code/python-transportation/train-model-YOLOv10/crop.jpg")
                        if result:
                            plate_number = result[0][1]
                            
                            cv2.putText(frame, plate_number, (x1, y1 - 30), font, fontScale, color, thickness, cv2.LINE_AA)
                            print(plate_number)
                            # Tạo nhãn để hiển thị giá trị biển số xe và sắp xếp bằng .grid()
                            label_plate = tk.Label(right_frame, text=plate_number, font=("Arial", 20))
                            label_plate.grid(row=0, column=0, padx=20, pady=20)
                    

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển đổi sang RGB
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            camera_label.imgtk = img  # Lưu tham chiếu để tránh bị garbage collected
            camera_label.configure(image=img)
        camera_label.after(10, lambda:update_frame(gui,camera_label,right_frame))  # Cập nhật khung hình sau 10ms

def load_gui(gui,camera_label,right_frame):
    start_camera(gui,camera_label= camera_label,right_frame=right_frame)