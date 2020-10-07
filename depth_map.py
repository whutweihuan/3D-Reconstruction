# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/9/12  10:43
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

# imgL = cv2.imread('images/left01.jpg', 0)
# imgR = cv2.imread('images/right01.jpg', 0)
#
imgL = cv2.imread('calibresult-left.png', 0)
imgR = cv2.imread('calibresult-right.png', 0)

# https://blog.csdn.net/weixin_43042467/article/details/108199785
# numDisparities 最大差异减去最小差异。该值总是大于零。在当前的实现中，该参数必须可以被16整除。
# BLOCKSIZE 匹配的块大小。它必须是> = 1的奇数。通常情况下，它应该在3…11的范围内。
# stereo = cv2.StereoSGBM_create(numDisparities=16, blockSize=13)
#Create Block matching object.
win_size = 5
stereo = cv2.StereoSGBM_create(minDisparity= 16,
 numDisparities = 11,
 blockSize = 5,
 uniquenessRatio = 5,
 speckleWindowSize = 5,
 speckleRange = 5,
 disp12MaxDiff = 1,
 P1 = 8*3*win_size**2,#8*3*win_size**2,
 P2 =32*3*win_size**2) #32*3*win_size**2)

disparity = stereo.compute(imgL,imgR)
# plt.imshow(disparity)
print(disparity)
plt.imshow(disparity,'gray')
cv2.imwrite('depth.png', disparity)
# cv2.imwrite('images/p.png', imgL)
plt.show()

# depth images to cloud point
# from open3d import *
#
# rgbd = create_rgbd_image_from_color_and_depth(imgL, disparity, convert_rgb_to_intensity = False)
# pcd = create_point_cloud_from_rgbd_image(rgbd, camera.PinholeCameraIntrinsic(
#             camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
#
# # flip the orientation, so it looks upright, not upside-down
# pcd.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
#
# draw_geometries([pcd])    # visualize the point cloud