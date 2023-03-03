from cv2 import VideoCapture
def get_active_cameras(scan_range: int):
    for camera in range(scan_range):
        capture = VideoCapture(camera)
        valid_cameras = []
        if capture.isOpened():
            valid_cameras.append(camera)
            return [str(x) for x in valid_cameras]

           








