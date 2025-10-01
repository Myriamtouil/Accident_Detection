# 🚨 Accident Detection with YOLOv11

This project explores **real-time accident detection** using **YOLOv11**.  
The system is designed to detect road accidents in traffic surveillance videos.

---

## 🔬 Methodology
1. **Input Video** (traffic camera feed)  
2. **YOLOv11** for detecting accident-related objects (vehicles, collisions, etc.)  
3. **Post-processing** to filter and classify accident events  
4. **Output** → Bounding boxes + alert system

![Pipeline](docs/accident_pipeline.png)

---

## 📂 Project Layout
- `dataset/` → training data samples  
- `experiments/` → Jupyter notebooks for testing & prototyping  
- `scripts/` → Python scripts (training, inference, evaluation)  
- `models/` → trained weights & configs  
- `results/` → evaluation plots & sample detections  
- `docs/` → pipeline figures  

---

## 🏃 Usage
```bash
python scripts/train.py
python scripts/infer.py --image dataset/test.jpg
```

---

## 📜 License
MIT License
