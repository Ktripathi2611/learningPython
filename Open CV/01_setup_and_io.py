"""
01: Setup and Image I/O
- Print OpenCV version
- Read an image
- Display an image
- Save an image
"""
import cv2

# Print OpenCV version
print("OpenCV Version:", cv2.__version__)

# Read an image from file
# cv2.imread() returns None if file not found
img = cv2.imread("sample.jpg")

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image!")
else:
    # Print image info
    print("Image loaded successfully!")
    print("Shape:", img.shape)  # (height, width, channels)
    
    # Display image in a window
    cv2.imshow("My Image", img)
    
    # Wait for key press (0 = wait forever)
    print("Press any key to close...")
    cv2.waitKey(0)
    
    # Close all windows
    cv2.destroyAllWindows()
    
    # Save image to file
    cv2.imwrite("output.jpg", img)
    print("Image saved as output.jpg")
