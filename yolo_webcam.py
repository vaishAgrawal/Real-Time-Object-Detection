from ultralytics import YOLO
import cv2

# 🔥 Load YOLOv8 model
model = YOLO("yolov8n.pt")  # NOTE: use yolov8n (nano) for faster inference

# 🎥 Initialize webcam
cap = cv2.VideoCapture(0)  # 0 is default webcam

if not cap.isOpened():
    print("❌ Could not open webcam")
    exit()

print("✅ Press 'q' to quit the webcam stream")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # 🖼️ Run YOLO inference
    results = model(frame, show=False)

    # 📦 Draw results on frame
    annotated_frame = results[0].plot()

    # 🖥️ Display frame
    cv2.imshow("YOLOv8 Webcam", annotated_frame)

    # ⏹️ Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Exiting...")
        break

# 🧹 Clean up
cap.release()
cv2.destroyAllWindows()
