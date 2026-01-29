# Beginner OpenCV Tutorial 🎓

A collection of 8 simple Python scripts to learn OpenCV from scratch.

## 📋 Prerequisites
- Python installed
- `sample.jpg` in this folder (a test image)
- `sample.mp4` in this folder (for the video tutorial)

## 🛠️ Setup
Install the required libraries:
```bash
pip install opencv-python numpy
```

## 🚀 Learning Path

1. **[01_setup_and_io.py](file:///d:/learning%20HUB/python/Open%20CV/01_setup_and_io.py)**
   - Topic 1-5: Reading, displaying, and saving images.
2. **[02_resize_and_flip.py](file:///d:/learning%20HUB/python/Open%20CV/02_resize_and_flip.py)**
   - Topic 6, 9-11: Changing size and flipping images.
3. **[03_morphology.py](file:///d:/learning%20HUB/python/Open%20CV/03_morphology.py)**
   - Topic 7-8: Advanced shape operations (Erosion/Dilation).
4. **[04_draw_transform.py](file:///d:/learning%20HUB/python/Open%20CV/04_draw_transform.py)**
   - Topic 12-14: Drawing shapes and moving/rotating images.
5. **[05_threshold_and_blur.py](file:///d:/learning%20HUB/python/Open%20CV/05_threshold_and_blur.py)**
   - Topic 15-18: Filters and making images black & white.
6. **[06_edges.py](file:///d:/learning%20HUB/python/Open%20CV/06_edges.py)**
   - Topic 19: Finding outlines/edges in images.
7. **[07_video_io.py](file:///d:/learning%20HUB/python/Open%20CV/07_video_io.py)**
   - Topic 20-21: How to work with video files.
8. **[08_webcam.py](file:///d:/learning%20HUB/python/Open%20CV/08_webcam.py)**
   - Topic 22: Using your computer's camera.

---

### 💡 Tips for Beginners:
- **BGR vs RGB**: Remember that OpenCV reads color as **Blue-Green-Red** (BGR) while most other software uses Red-Green-Blue (RGB).
- **Coordinates**: (0,0) is the top-left corner of the image.
- **Quit**: Most scripts use `cv2.waitKey(0)` to wait for you. Press **any key** (or 'q' where specified) to close windows.
