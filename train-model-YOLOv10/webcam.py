import cv2
from ultralytics import YOLO
import read_plate

# Load the model
model = YOLO(f"D:\\code\\python-transportation\\train-model-YOLOv10\\best.pt")



# Mở webcam (0 là chỉ số của camera đầu tiên)
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 1)
            print("cls:",boxes.cls)
            # class name
            labels = str(box.cls)
            if hasattr(box, 'label'):
                labels = box.label[0]
                print("Label:", labels)
            else:
                print("No label found for this box")
            
            # object details
            org = (x1, y1 - 10)  # Vẽ nhãn ngay phía trên hộp bao
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            # Draw the label text on the image
            cv2.putText(img, labels, org, font, fontScale, color, thickness)

             # Crop the image to the bounding box
            cropped_img = img[y1:y2, x1:x2]
            resized_cropped_img = cv2.resize(cropped_img, (200, 200))
            cv2.imshow('Cropped Image', resized_cropped_img)
            results=read_plate.read_license_plate(resized_cropped_img)
            print("Results:",results)
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()