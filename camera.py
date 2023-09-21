# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


video =cv2.VideoCapture(0)
video.set(3, 640)
video.set(4, 480)

while True:
  ret, frame = video.read()
  bbox, label, conf = cv.detect_common_objects(frame)
  output_image = draw_bbox(frame, bbox, label, conf)

  cv2.imshow('Plant Detection test', output_image)

  if cv2.waitKey(1) & 0xFF ==ord('q'):
    break


