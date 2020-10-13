# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/9/30  16:38
"""
import cv2
# 笔记本本身摄像头
cap0 = cv2.VideoCapture(0);
cap0.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# 两个摄像头放在一起
cap1 = cv2.VideoCapture(1);
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

index = 1;
while True:
    # ret0, frame1 = cap0.read()
    ret1, frame_both = cap1.read()
    frame1 = frame_both[:, 0:640, :]
    frame2 = frame_both[:, 640:, :]

    # print('Retval cap0: ' ,ret0)
    # print('Retval cap1: ', ret1)

    # if ret0:
    #         cv2.imshow('frame1', frame1)
    # if ret1:
    #         cv2.imshow('frame2', frame2)

    # if ret0 and ret1:
    if ret1:
        # cv2.imshow('frame1', frame_both)
        cv2.imshow('frame1', frame1)
        cv2.imshow('frame2', frame2)

    push_key = cv2.waitKey(100)
    # print(push_key)

    if push_key == ord('t'):
        cv2.imwrite('snapshot/'+"%03d_left" % index +'.png',frame1)
        cv2.imwrite('snapshot/'+"%03d_right" % index +'.png',frame2)
        cv2.imwrite('snapshot/'+"%03d_both" % index +'.png',frame_both)
        print('捕获图片 %03d' % index)
        index+=1
    elif push_key == ord('q'):
        break


cap0.release()
cap1.release()
cv2.destroyAllWindows()