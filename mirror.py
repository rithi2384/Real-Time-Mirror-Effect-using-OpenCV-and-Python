import cv2 # type: ignore

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Mirror effect
    mirror = cv2.flip(frame, 1)

    # Convert to gray
    gray = cv2.cvtColor(mirror, cv2.COLOR_BGR2GRAY)

    # Edge detection (sketch effect)
    sketch = cv2.Canny(gray, 50, 150)

    # Show outputs
    cv2.imshow("Mirror Camera", mirror)
    cv2.imshow("Sketch Camera", sketch)

    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
