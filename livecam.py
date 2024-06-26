import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

images = []

print("Press 'c' to capture an image, 's' to stitch and show panorama, 'q' to quit.")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    cv2.imshow('Webcam', frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('c'):
        images.append(frame)
        print(f"Captured image {len(images)}")
    
    
    elif key == ord('s'):
        if len(images) < 2:
            print("Need at least 2 images to stitch.")
            continue
        
        stitcher = cv2.Stitcher.create()
        (status, panorama) = stitcher.stitch(images)
        
        if status == cv2.STITCHER_OK:
            print('Generated panorama')
            cv2.imshow('Panorama', panorama)
        else:
            print(f"Error: Unable to generate panorama, status code: {status}")
    

    elif key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
