from ultralytics import YOLO
model = YOLO(r"C:\Users\tuana\Downloads\Front.pt")
model.export(format = 'engine')