import cv2 as cv
import numpy as np

cap = cv.VideoCapture("C:\\Users\\DAREWIN\\Base de donne\\DB LSF Mots\\20_vouloir\\00360.MTS")

frame_count = 0
all_frames = []
while True:
    (ret, frame) = cap.read()
    if ret is False:
        break
    all_frames.append(frame)
    cv.imwrite("C:\\Users\\DAREWIN\\Base de donne\\DB LSF Mots\\20_vouloir\\190\\%04d" % frame_count + ".jpg", frame)
    frame_count += 1

print(frame_count)
# print(len(all_frames))


frame1 = all_frames[0]