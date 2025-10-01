import argparse
from ultralytics import YOLO

def run_inference(image_path):
    model = YOLO("results/accident_detection/weights/best.pt")
    results = model(image_path)
    results.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True)
    args = parser.parse_args()
    run_inference(args.image)
