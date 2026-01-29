"""
07: Video I/O
- Read video file
- Write video file
"""
import cv2

# Open video file (change to your video path)
cap = cv2.VideoCapture("walkthrough.mp4")

# Check if video opened
if not cap.isOpened():
    print("Error: Could not open video!")
    print("Make sure sample.mp4 exists in this folder")
else:
    # Get video info
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Video: {width}x{height} at {fps} FPS")
    
    # Setup video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
    
    # Read and display frames
    while True:
        ret, frame = cap.read()
        
        # ret is False if no more frames
        if not ret:
            print("End of video")
            break
        
        # Add text to frame
        cv2.putText(frame, "Recording...", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Write frame to output video
        out.write(frame)
        
        # Display frame
        cv2.imshow("Video", frame)
        
        # Press 'q' to quit early
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    # Cleanup
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Video saved as output.avi")
