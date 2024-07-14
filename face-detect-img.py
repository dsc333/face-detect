'''
Installation:
python3 -m venv --system-site-packages env
source env/bin/activate
pip3 install opencv-contrib-python
pip3 install mediapipe
'''

import cv2
from picamera2 import Picamera2, Preview
import numpy as np
import mediapipe as mp
from PIL import Image

img_path = './face.jpg'
img = cv2.imread(img_path)

# Get image dimensions
img_h, img_w, _ = img.shape

# detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, 
                                     min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    print(out.detections)            

    # extract the locations of the bounding boxes for each detected face
    for detection in out.detections:
        location_data = detection.location_data
        bbox = location_data.relative_bounding_box

        # Get relative coordinates and convert to absolute pixel values
        x1 = int(bbox.xmin * img_w) 
        y1 = int(bbox.ymin * img_h) 
        w = int(bbox.width * img_w) 
        h = int(bbox.height * img_h)

        # Draw rectangle around the bounding box of faces detected
        img = cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 255, 0), 5)

    cv2.imshow("image", img)
    key = cv2.waitKey(0)

    if key == ord('q'):
        cv2.destroyAllWindows()
                 
        
'''
# Initialize camera
camera = Picamera2()
while True:
    camera.start()

    # Capture frame from camera and resize it
    frame = camera.capture_array()
    frame_small = cv2.resize(frame, (640, 480))
    rgb_img = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)
    hsv_img = cv2.cvtColor(frame_small, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=lime)
    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)

    # convert mask to image
    mask_img = Image.fromarray(mask)

    # Get bounding box of the object represented in the mask
    bbox = mask_img.getbbox()

    # If bounding box exists, get its coordinates and draw a rectangle over it
    if bbox:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
    cv2.imshow('frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
