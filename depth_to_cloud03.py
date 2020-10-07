# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/9/13  12:14
"""
# 参考链接
# https://www.zhihu.com/question/268488496
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import cv2
import numpy as np

ox = 480 / 2
oy = 640 / 2
fx = 480 / (2 * np.tan(0.5 * np.pi * 90 / 180))
fy = 640 / (2 * np.tan(0.5 * np.pi * 59 / 180))

depth_bg = cv2.imread('depth.png', -1)
gridyy, gridxx = np.mgrid[:480, :640]

xx_cam = (gridxx - ox) / fx * depth_bg
yy_cam = (gridyy - oy) / fy * depth_bg

depth_bg = depth_bg[..., np.newaxis]
bg_xyz = np.concatenate((xx_cam[..., np.newaxis], yy_cam[..., np.newaxis], depth_bg), axis=2)
bg_xyz_resh_all = np.reshape(bg_xyz, (-1, 3))
bg_xyz_resh = bg_xyz_resh_all[bg_xyz_resh_all[:, 2] > 0]

fig = plt.figure()
ax = mplot3d.Axes3D(fig)

xyzs = bg_xyz_resh

ax.scatter3D(xyzs.T[0], xyzs.T[1], xyzs.T[2])  # 散点图
plt.show()