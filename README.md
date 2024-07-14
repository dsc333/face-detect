# Face detection

Detects and blurs faces in an image.  Uses mediapipe (for face detection) and OpenCV for blurring.

**Installation Instructions:**
1. git clone https://github.com/dsc333/face-detect
2. cd face-detect
3. python3 -m venv --system-site-packages env
4. source env/bin/activate
5. pip3 install opencv-contrib-python
6. pip3 install mediapipe
7. Options:
   1. python3 face-detect-img.py (detects faces detected in image)
   2.  python3 face-blur-img.py (blurs faces detected in an image) 
8. Press 'q' to quit the program
9. Type: deactivate when done
