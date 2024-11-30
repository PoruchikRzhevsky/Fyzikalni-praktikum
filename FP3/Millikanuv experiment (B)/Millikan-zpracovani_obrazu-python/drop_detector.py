import cv2
import numpy as np


def find_drops(frame: cv2.UMat, min_thresh: int, max_thresh: int):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, min_thresh, max_thresh, cv2.THRESH_BINARY)[1]
    (spotsCount, labels, stats, centroids) = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)

    drops = []
    for i in range(1, spotsCount):
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        drops.append((x, y, w, h))

    return drops

def request_threshold(frame: cv2.UMat):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("thresh")
    cv2.createTrackbar("min", "thresh", 0, 255, lambda x: None)
    cv2.createTrackbar("max", "thresh", 0, 255, lambda x: None)
    cv2.setTrackbarPos("min", "thresh", 80)
    cv2.setTrackbarPos("max", "thresh", 255)
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        threshMin = cv2.getTrackbarPos("min", "thresh")
        threshMax = cv2.getTrackbarPos("max", "thresh")

        thresh = cv2.threshold(gray, threshMin, threshMax, cv2.THRESH_BINARY)[1]
        cv2.imshow("thresh", thresh)

    cv2.destroyWindow("thresh")
    return threshMin, threshMax