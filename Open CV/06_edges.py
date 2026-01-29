"""
06: Edge Detection
- Canny edge detection
"""
import cv2

# Read image
img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Could not load image!")
else:
    # Convert to grayscale (required for edge detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny edge detection
    # threshold1, threshold2: lower = more edges, higher = fewer edges
    edges = cv2.Canny(blurred, 100, 200)
    
    # Try different thresholds
    edges_more = cv2.Canny(blurred, 50, 100)   # More edges
    edges_less = cv2.Canny(blurred, 150, 250)  # Fewer edges
    
    # Show results
    cv2.imshow("Original", cv2.resize(img, (400, 300)))
    cv2.imshow("Edges (100-200)", cv2.resize(edges, (400, 300)))
    cv2.imshow("More Edges (50-100)", cv2.resize(edges_more, (400, 300)))
    cv2.imshow("Fewer Edges (150-250)", cv2.resize(edges_less, (400, 300)))
    
    print("Press any key to close...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
