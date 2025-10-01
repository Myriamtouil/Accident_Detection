from ultralytics import YOLO

def evaluate_model():
    model = YOLO("results/accident_detection/weights/best.pt")
    metrics = model.val()
    print(metrics)

if __name__ == "__main__":
    evaluate_model()
