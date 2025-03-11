import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk

def start_camera():
    global cap, camera_running
    camera_running = True
    cap = cv2.VideoCapture(0)  # Sử dụng camera mặc định
    update_frame()

def stop_camera():
    global camera_running
    camera_running = False
    if cap.isOpened():
        cap.release()  # Dừng camera

def update_frame():
    if camera_running and cap.isOpened():
        ret, frame = cap.read()  # Đọc một khung hình từ camera
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển đổi sang RGB
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            camera_label.imgtk = img  # Lưu tham chiếu để tránh bị garbage collected
            camera_label.configure(image=img)
        camera_label.after(10, update_frame)  # Cập nhật khung hình sau 10ms

# Giao diện Tkinter
gui = tk.Tk()
gui.title("Cửa sổ Camera")
gui.geometry("800x600")

camera_label = Label(gui)
camera_label.pack(pady=20)

start_button = tk.Button(gui, text="Bật Camera", command=start_camera)
start_button.pack(pady=10)

stop_button = tk.Button(gui, text="Tắt Camera", command=stop_camera)
stop_button.pack(pady=10)

gui.protocol("WM_DELETE_WINDOW", lambda: [stop_camera(), gui.destroy()])
gui.mainloop()
