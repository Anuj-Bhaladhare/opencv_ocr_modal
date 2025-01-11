import cv2
import os
import numpy as np

# Open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise Exception("Webcam not found or cannot be accessed!")

print("Press 's' to capture a photo and 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):  # Save the photo
        temp_path = "temp_photo.jpg"
        cv2.imwrite(temp_path, frame)
        print(f"Photo saved to {temp_path}")
        break
    elif key == ord('q'):  # Quit
        break

cap.release()
cv2.destroyAllWindows()

# Load the saved photo
image = cv2.imread(temp_path)

# Convert to grayscale and detect edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# Detect lines using Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

if lines is not None:
    angles = [np.rad2deg(theta) - 90 for rho, theta in lines[:, 0]]
    median_angle = np.median(angles)
    nearest_90 = round(median_angle / 90) * 90

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, nearest_90, 1.0)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    corrected_path = "corrected_photo.jpg"
    cv2.imwrite(corrected_path, rotated)
    print(f"Corrected photo saved as {corrected_path}. Rotated by {nearest_90} degrees.")

    cv2.imshow("Original Photo", image)
    cv2.imshow("Corrected Photo", rotated)
else:
    print("No dominant orientation detected. Image remains unchanged.")
    cv2.imshow("Original Photo", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Cleanup temporary file
if os.path.exists(temp_path):
    os.remove(temp_path)
