"""
02: Resize and Flip
- Resize image to fixed size
- Resize by percentage
- Flip horizontally and vertically
"""
import cv2

# Read image
img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Could not load image!")
else:
    print("Original size:", img.shape[:2])  # (height, width)
    
    # --- RESIZE ---
    
    # Method 1: Resize to exact size (width, height)
    resized = cv2.resize(img, (400, 300))
    print("Resized to 400x300:", resized.shape[:2])
    
    # Method 2: Resize by scale (50% = 0.5)
    half = cv2.resize(img, None, fx=0.5, fy=0.5)
    print("Resized to 50%:", half.shape[:2])
    
    # Method 3: Resize keeping aspect ratio
    height, width = img.shape[:2]
    new_width = 400
    new_height = int(height * new_width / width)
    aspect_resized = cv2.resize(img, (new_width, new_height))
    print("Aspect ratio resize:", aspect_resized.shape[:2])
    
    # --- FLIP ---
    
    # Flip horizontally (mirror)
    flip_h = cv2.flip(img, 1)
    
    # Flip vertically (upside down)
    flip_v = cv2.flip(img, 0)
    
    # Flip both ways
    flip_both = cv2.flip(img, -1)
    
    # Show results
    cv2.imshow("Original", cv2.resize(img, (300, 200)))
    cv2.imshow("Horizontal Flip", cv2.resize(flip_h, (300, 200)))
    cv2.imshow("Vertical Flip", cv2.resize(flip_v, (300, 200)))
    
    print("Press any key to close...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
