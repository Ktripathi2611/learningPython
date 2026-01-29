"""
04: Drawing Shapes, Text & Transformations
- Draw rectangle, circle, line
- Add text
- Move image (translation)
- Rotate image
"""
import cv2
import numpy as np

# Read image
img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Could not load image!")
else:
    # Make a copy for drawing
    canvas = img.copy()
    
    # --- DRAW SHAPES ---
    
    # Draw rectangle (green, thickness 2)
    cv2.rectangle(canvas, (50, 50), (200, 150), (0, 255, 0), 2)
    
    # Draw filled rectangle (red, thickness -1 = filled)
    cv2.rectangle(canvas, (250, 50), (400, 150), (0, 0, 255), -1)
    
    # Draw circle (blue)
    cv2.circle(canvas, (150, 250), 50, (255, 0, 0), 2)
    
    # Draw line (yellow)
    cv2.line(canvas, (50, 350), (300, 350), (0, 255, 255), 3)
    
    # Add text (white)
    cv2.putText(canvas, "Hello OpenCV!", (50, 400), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # --- TRANSLATION (MOVE IMAGE) ---
    
    height, width = img.shape[:2]
    
    # Move 100 pixels right, 50 pixels down
    M_move = np.float32([[1, 0, 100], [0, 1, 50]])
    moved = cv2.warpAffine(img, M_move, (width, height))
    
    # --- ROTATION ---
    
    # Rotate 45 degrees around center
    center = (width // 2, height // 2)
    M_rotate = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(img, M_rotate, (width, height))
    
    # Show results
    cv2.imshow("Shapes & Text", cv2.resize(canvas, (400, 300)))
    cv2.imshow("Moved", cv2.resize(moved, (400, 300)))
    cv2.imshow("Rotated", cv2.resize(rotated, (400, 300)))
    
    print("Press any key to close...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
