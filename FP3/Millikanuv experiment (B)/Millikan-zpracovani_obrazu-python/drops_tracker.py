from dataclasses import dataclass
from typing import List, Tuple

import cv2
import numpy as np
from drop_detector import find_drops

DROP_PX_MARGIN = 8

@dataclass
class DropTracker:
    bbox: Tuple[int, int, int, int]
    tracker: cv2.TrackerMIL
    init_frame: int
    active: bool

class DropsTracker:
    def __init__(self, init_frame, drops, thresh_min, thresh_max, vid_resolution: Tuple[int, int]) -> None:
        self.frame_i = 0
        self.trackers: List[DropTracker] = []

        for drop in drops:
            drop_bbox = self.detected_drop_to_bbox(drop, vid_resolution)
            tracker = cv2.TrackerMIL_create()
            tracker.init(init_frame, drop_bbox)
            drop_tracker = DropTracker(drop_bbox, tracker, 0, True)
            self.trackers.append(drop_tracker)

        self.thresh_min = thresh_min
        self.thresh_max = thresh_max
        

    def track(self, frame: cv2.UMat):
        self.frame_i += 1
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for drop_tracker in self.get_active_trackers():
            ok, bbox = drop_tracker.tracker.update(frame)

            # check if drop is still visible
            drop_frame = grey[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]
            drop_std = cv2.meanStdDev(drop_frame)[1][0][0]
            if drop_std < 5:
                ok = False
            if not ok:
                drop_tracker.active = False
                continue
            
            drop_tracker.bbox = bbox

        # Add/reset new drops
        detected_drops = find_drops(frame, self.thresh_min, self.thresh_max)
        for detected_drop in detected_drops:
            drop_tracker = self.get_drop_tracker(detected_drop)
            if drop_tracker is None:
                bbox = self.detected_drop_to_bbox(detected_drop, frame.shape[:2])
                tracker = cv2.TrackerMIL_create()
                tracker.init(frame, bbox)
                drop_tracker = DropTracker(bbox, tracker, self.frame_i, True)
                self.trackers.append(drop_tracker)
            else:
                tracked_bbox = self.detected_drop_to_bbox(detected_drop, frame.shape[:2])
                new_tracker = cv2.TrackerMIL_create()
                new_tracker.init(frame, tracked_bbox)
                drop_tracker.tracker = new_tracker

        # Remove overlapping trackers
        for drop_tracker in self.trackers:
            for other_drop_tracker in self.trackers:
                if drop_tracker == other_drop_tracker:
                    continue
                bbox = drop_tracker.bbox
                other_bbox = other_drop_tracker.bbox
                other_drop_center = (other_bbox[0] + other_bbox[2] / 2, other_bbox[1] + other_bbox[3] / 2)
                if (other_drop_center[0] > bbox[0] and other_drop_center[0] < bbox[0] + bbox[2] and
                    other_drop_center[1] > bbox[1] and other_drop_center[1] < bbox[1] + bbox[3]):
                    if drop_tracker.init_frame > other_drop_tracker.init_frame:
                        drop_tracker.active = False
                    else:
                        other_drop_tracker.active = False
                    
    def get_drop_tracker(self, drop: Tuple[int, int, int, int]):
        drop_center = (drop[0] + drop[2] / 2, drop[1] + drop[3] / 2)
        for drop_tracker in self.trackers:
            tracked_bbox = drop_tracker.bbox
            tracked_drop_center = (tracked_bbox[0] + tracked_bbox[2] / 2, tracked_bbox[1] + tracked_bbox[3] / 2)
            drop_diff = (tracked_drop_center[0] - drop_center[0], tracked_drop_center[1] - drop_center[1])
            drop_r = np.sqrt(drop_diff[0] ** 2 + drop_diff[1] ** 2)
            if (drop_r < 20):
                return drop_tracker
        return None

    def detected_drop_to_bbox(self, drop: Tuple[int, int, int, int], frame_size: Tuple[int, int]):
        bbox = [drop[0] - DROP_PX_MARGIN, drop[1] - DROP_PX_MARGIN, drop[2] + DROP_PX_MARGIN * 2, drop[3] + DROP_PX_MARGIN * 2]
        if bbox[0] < 0:
            bbox[0] = 0
        if bbox[0] + bbox[2] > frame_size[1]:
            bbox[2] = frame_size[1] - bbox[0]
        if bbox[1] < 0:
            bbox[1] = 0
        if bbox[1] + bbox[3] > frame_size[0]:
            bbox[3] = frame_size[0] - bbox[1]
        return bbox

    def get_active_trackers(self):
        return [drop_tracker for drop_tracker in self.trackers if drop_tracker.active]
        



