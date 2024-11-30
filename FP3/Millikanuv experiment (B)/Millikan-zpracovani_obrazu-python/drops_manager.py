
from ast import List
from dataclasses import dataclass
import numpy as np
from drops_tracker import DropTracker


@dataclass
class DropLog:
    frame_i: int
    x: np.ndarray
    y: np.ndarray


class DropsManager:
    def __init__(self, video_file: str):
        self.drop_logs: List[DropLog] = []
        self.video_file = video_file
    
    def log_drops(self, frame_i, drop_trackers: List(DropTracker)):
        x = np.array([(drop_tracker.bbox[0] if drop_tracker.active else np.nan) for drop_tracker in drop_trackers])
        y = np.array([(drop_tracker.bbox[1] if drop_tracker.active else np.nan) for drop_tracker in drop_trackers])
        self.drop_logs.append(DropLog(frame_i, x, y))
    
    def save(self):
        total_drops = len(self.drop_logs[-1].x)

        drop_table_x = np.zeros((len(self.drop_logs), total_drops + 1))
        drop_table_x[:, 0] = np.arange(len(self.drop_logs))
        drop_table_x[:, 1:] = np.array([_ndarray_to_fixed_len(drop_log.x, total_drops) for drop_log in self.drop_logs])

        drop_table_y = np.zeros((len(self.drop_logs), total_drops + 1))
        drop_table_y[:, 0] = np.arange(len(self.drop_logs))
        drop_table_y[:, 1:] = np.array([_ndarray_to_fixed_len(drop_log.y, total_drops) for drop_log in self.drop_logs])

        np.savetxt(self.video_file + "_x.csv", drop_table_x, delimiter=",")
        np.savetxt(self.video_file + "_y.csv", drop_table_y, delimiter=",")
        
def _ndarray_to_fixed_len(arr: np.ndarray, length: int, fill_value: int = np.nan):
    if len(arr) >= length:
        return arr[:length]
    else:
        return np.concatenate((arr, np.full(length - len(arr), fill_value)))
    