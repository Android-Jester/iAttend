import cv2
from cv2 import VideoCapture

valid_cameras = []
# def get_active_cameras(scan_range: int):
#     for camera in range(scan_range):
#         capture = VideoCapture(camera)
#         if capture.isOpened():
#             valid_cameras.append(camera)

def get_active_cameras(scan_range: int):
    for camera in range(scan_range):
        valid_cameras.append(camera)

def return_active_cameras(scan_range: int):
    get_active_cameras(scan_range)
    return [str(x) for x in valid_cameras]




