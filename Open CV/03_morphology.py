"""
03: Morphological Operations
- Erosion (shrink white areas)
- Dilation (expand white areas)
- Opening (remove noise)
- Closing (fill holes)
"""
import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not load image!")
else:
    # Convert to binary (black and white only)
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    # Create a 5x5 kernel (small square)
    kernel = np.ones((5, 5), np.uint8)
    
    # Erosion - shrinks white regions
    erosion = cv2.erode(binary, kernel, iterations=1)
    
    # Dilation - expands white regions
    dilation = cv2.dilate(binary, kernel, iterations=1)
    
    # Opening = Erosion + Dilation (removes small white noise)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    # Closing = Dilation + Erosion (fills small black holes)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    # Show results
    cv2.imshow("Binary", binary)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Dilation", dilation)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)
    
    print("Press any key to close...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
