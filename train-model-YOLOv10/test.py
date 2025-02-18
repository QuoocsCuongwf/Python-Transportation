from ultralytics import YOLO

# Load the model
model = YOLO(f'best.pt')

# Run inference
results = model(source='th.png', conf=0.1, save=True)
print(results)