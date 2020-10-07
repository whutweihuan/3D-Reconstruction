# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/9/12  19:56
"""
import os
import numpy as np
from open3d import *


points = np.random.rand(10000, 3)
point_cloud = PointCloud()
point_cloud.points = Vector3dVector(points)
draw_geometries([point_cloud])