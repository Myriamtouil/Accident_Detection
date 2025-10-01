from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.pt")  # YOLOv11 small model for testing
    model.train(
        data="dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        project="./results",
        name="accident_detection"
        # Parameters tuned internally, hidden for clarity
    )

if __name__ == "__main__":
    train_model()
