import cv2
import numpy as np
import argparse
from background_remover import BackgroundRemover
from drops_manager import DropsManager

from drop_detector import find_drops, request_threshold
from drops_tracker import DropsTracker

DROP_PX_SIZE = 10

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        prog = "kapkal",
        description = "Kapkal is a tool for tracking drops in a video.",
        epilog = "Example: python3 kapkal.py --min-b 80 data/vids/300_1.mpg"
    )

    argparser.add_argument("video_files", help="Path to video files", nargs="+")
    argparser.add_argument("--min-b", help="Minimum brightness threshold", type=int, default=0)
    argparser.add_argument("--max-b", help="Maximum brightness threshold", type=int, default=255)
    argparser.add_argument("--brightness", help="Brightness", type=float, default=1)
    argparser.add_argument("--contrast", help="Contrast", type=float, default=3)
    argparser.add_argument("--blur", help="Blur", type=float, default=3)

    args = argparser.parse_args()

    video_files = args.video_files
    threshMin = args.min_b
    threshMax = args.max_b
    brightness = args.brightness
    contrast = args.contrast
    blur = args.blur

    for video_file in video_files:
        background_remover = BackgroundRemover()
        background_remover.train(video_file)

        video = cv2.VideoCapture(video_file)
        # Play video with background removed
        ret, frame = video.read()
        if ret == False:
            print("Error reading video")
            exit(1)
        while True:
            ret, frame = video.read()
            if ret == False:
                break

            frame = background_remover.remove_background(frame)
            frame = cv2.medianBlur(frame, blur)
            frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)
            cv2.imshow("frame", frame)
            cv2.setWindowTitle("frame", "Background removed (press q to continue)")

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        # Reopen video
        video.release()
        video = cv2.VideoCapture(video_file)
        ret, frame = video.read()

        frame = cv2.medianBlur(frame, blur)
        frame = background_remover.remove_background(frame)
        # Increase contrast
        frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows = gray.shape[0]

        if threshMin == 0:
            threshMin, threshMax = request_threshold(frame)
        init_drops = find_drops(frame, threshMin, threshMax)
        drops_tracker = DropsTracker(frame, init_drops, threshMin, threshMax, frame.shape[:2])
        drops_manager = DropsManager(video_file)

        while True:
            ret, frame = video.read()
            if ret == False:
                break

            # Increase contrast
            frame = background_remover.remove_background(frame)
            frame = cv2.medianBlur(frame, blur)
            frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

            drops = find_drops(frame, threshMin, threshMax)
            drops_tracker.track(frame)

            # draw bounding boxes - drops
            for bbox in drops:
                cv2.rectangle(frame, bbox[0:2], (bbox[0]+bbox[2], bbox[1]+bbox[3]), (0, 0, 255), 2)

            # draw bounding boxes - tracked drops
            for drop_tracker in drops_tracker.get_active_trackers():
                bbox = drop_tracker.bbox
                pt1 = (int(bbox[0]), int(bbox[1]))
                pt2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 2)
            
            drops_manager.log_drops(drops_tracker.frame_i, drops_tracker.trackers)

            print(f"Frame {drops_tracker.frame_i}: Found {len(drops)} drops, tracked {len(drops_tracker.trackers)} drops, active {len(drops_tracker.get_active_trackers())}")
            cv2.imshow("frame", frame)
            cv2.setWindowTitle("frame", f"Video: {video_file}, frame: {drops_tracker.frame_i} / {int(video.get(cv2.CAP_PROP_FRAME_COUNT))}")
            cv2.waitKey(10)
            
        drops_manager.save()
        video.release()
        cv2.destroyWindow("frame")
    
    cv2.destroyAllWindows()