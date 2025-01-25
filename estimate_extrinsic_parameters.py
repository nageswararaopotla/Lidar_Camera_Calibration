import cv2
import numpy as np

# Assuming `image_corners` is Nx2 array from camera and `lidar_corners` is Nx3 array from LiDAR

# Camera intrinsic parameters (for example purposes, should be calibrated beforehand)
camera_matrix = np.array([[fx, 0, cx],
                          [0, fy, cy],
                          [0, 0, 1]])
dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion

# Solve PnP to find the rotation and translation vectors
ret, rvec, tvec = cv2.solvePnP(lidar_corners, image_corners, camera_matrix, dist_coeffs)

if ret:
    # Convert rotation vector to matrix
    R, _ = cv2.Rodrigues(rvec)
    T = tvec
    
    # Extrinsic matrix
    extrinsic_matrix = np.hstack((R, T))
    
    print("Extrinsic parameters:")
    print("Rotation matrix:\n", R)
    print("Translation vector:\n", T)
else:
    print("PnP solution couldn't be found.")
