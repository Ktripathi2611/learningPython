"""
05: Thresholding and Blur
- Convert to grayscale
- Binary threshold
- Gaussian blur
- Median blur
- Bilateral filter
"""
import cv2

# Read image
img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Could not load image!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # --- THRESHOLDING ---
    
    # Binary threshold: pixels > 127 become white, else black
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Otsu's threshold (auto finds best threshold)
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # --- BLUR FILTERS ---
    
    # Gaussian blur (smooth blur)
    gaussian = cv2.GaussianBlur(img, (7, 7), 0)
    
    # Median blur (good for salt-pepper noise)
    median = cv2.medianBlur(img, 7)
    
    # Bilateral filter (blur but keep edges sharp)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    
    # Show results
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Binary Threshold", thresh)
    cv2.imshow("Otsu Threshold", otsu)
    cv2.imshow("Gaussian Blur", cv2.resize(gaussian, (400, 300)))
    cv2.imshow("Median Blur", cv2.resize(median, (400, 300)))
    cv2.imshow("Bilateral Filter", cv2.resize(bilateral, (400, 300)))
    
    print("Press any key to close...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
