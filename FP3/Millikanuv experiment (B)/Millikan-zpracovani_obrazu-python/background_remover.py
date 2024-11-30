import cv2
import numpy as np

from typing import List, Tuple

class BackgroundRemover:
    
    def train(self, video_file: str):
        cap = cv2.VideoCapture(video_file)
        ret, frame = cap.read()

        # convert frame to 32bit image
        print(video_file)
        print(frame)

        # convert frame to 32bit image
        if frame is None:
            raise ValueError("Frame is None. Check if the video file is correct and readable.")
        else:
            self.bg = frame.astype(np.float32)


        cv2.namedWindow("background-training")
        cv2.imshow("background-training", self.bg)
        frame_count = 0
        while cap.isOpened():
            frame_count += 1
            ret, frame = cap.read()
            if not ret:
                break
            cv2.accumulate(frame, self.bg)
            cv2.imshow("background-training", (self.bg / frame_count).astype(np.uint8))
            cv2.waitKey(5)

        cap.release()
        self.bg = (self.bg / frame_count).astype(np.uint8)
        cv2.destroyWindow("background-training")
        
    
    def remove_background(self, frame: cv2.UMat):
        return cv2.absdiff(frame, self.bg)