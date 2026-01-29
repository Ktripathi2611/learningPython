"""
08: Webcam
- Access webcam
- Show live video
- Apply effects
"""
import cv2

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if webcam opened
if not cap.isOpened():
    print("Error: Could not open webcam!")
else:
    print("Webcam is running...")
    print("Press 'q' to quit")
    print("Press 'g' for grayscale")
    print("Press 'e' for edges")
    print("Press 'n' for normal")
    
    mode = "normal"
    
    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Error reading frame")
            break
        
        # Apply effect based on mode
        if mode == "gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif mode == "edge":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.Canny(gray, 100, 200)
        
        # Show mode on screen
        if len(frame.shape) == 2:  # Grayscale
            display = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        else:
            display = frame
        cv2.putText(display, f"Mode: {mode}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display frame
        cv2.imshow("Webcam", display)
        
        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('g'):
            mode = "gray"
        elif key == ord('e'):
            mode = "edge"
        elif key == ord('n'):
            mode = "normal"
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Webcam closed")
