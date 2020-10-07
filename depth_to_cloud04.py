# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/10/7  19:10
"""
#Generate  point cloud.
import cv2
import numpy as np


print ("\nGenerating the 3D map...")
#Get new downsampled width and height
h,w = img_2_downsampled.shape[:2]
#Load focal length.
focal_length = np.load('./camera_params/FocalLength.npy')
#Perspective transformation matrix
#This transformation matrix is from the openCV documentation, didn't seem to work for me.
Q = np.float32([[1,0,0,-w/2.0],
    [0,-1,0,h/2.0],
    [0,0,0,-focal_length],
    [0,0,1,0]])
#This transformation matrix is derived from Prof. Didier Stricker's power point presentation on computer vision.
#Link : https://ags.cs.uni-kl.de/fileadmin/inf_ags/3dcv-ws14-15/3DCV_lec01_camera.pdf
Q2 = np.float32([[1,0,0,0],
    [0,-1,0,0],
    [0,0,focal_length*0.05,0], #Focal length multiplication obtained experimentally.
    [0,0,0,1]])
#Reproject points into 3D
points_3D = cv2.reprojectImageTo3D(disparity_map, Q2)
#Get color points
colors = cv2.cvtColor(img_1_downsampled, cv2.COLOR_BGR2RGB)
#Get rid of points with value 0 (i.e no depth)
mask_map = disparity_map > disparity_map.min()
#Mask colors and points.
output_points = points_3D[mask_map]
output_colors = colors[mask_map]
#Define name for output file
output_file = 'reconstructed.ply'
#Generate point cloud
print ("\n Creating the output file... \n")
create_output(output_points, output_colors, output_file)