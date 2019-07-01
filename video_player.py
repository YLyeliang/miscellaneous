import cv2
import os

path="D:/video/"
video_path=os.path.join(path,os.listdir(path)[0])
print(video_path)

cap=cv2.VideoCapture(video_path)
fps_num = int(cap.get(cv2.CAP_PROP_FPS))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
loop_flag = 0
pos =0
cv2.namedWindow("video",cv2.WINDOW_NORMAL)
cv2.createTrackbar("progress","video",0,frames,lambda x:None)

# def onTrackbarSlide(pos):


while True:
    if loop_flag == pos:
        loop_flag = loop_flag +1
        cv2.setTrackbarPos('progress','video',loop_flag)
    else:
        pos = cv2.getTrackbarPos('progress','video')
        loop_flag = pos
        cap.set(cv2.CAP_PROP_POS_FRAMES,pos)

    ret,frame=cap.read()
    cv2.imshow("video",frame)
    if cv2.waitKey(1) &0xff== ord('q'):
        break