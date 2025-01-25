import cv2
import numpy as np

# Load camera image
image = cv2.imread('camera_image.jpg')

# Define the checkerboard pattern dimensions
checkerboard_dims = (9, 6)  # Number of inner corners per a chessboard row and column

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, checkerboard_dims, None)

if ret:
    # Refine the corner locations
    corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    
    # Draw and display the corners
    cv2.drawChessboardCorners(image, checkerboard_dims, corners, ret)
    cv2.imshow('Chessboard Corners', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Checkerboard couldn't be detected in the camera image.")
