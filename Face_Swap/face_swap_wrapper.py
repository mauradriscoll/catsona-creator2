#! /usr/bin/env python
import os
import cv2
import argparse
from Face_Swap.face_detection import select_face
from Face_Swap.face_swap import face_swap

def fs_wrapper(src,dest):
 '''function that takes in two images and is 
    used to produce face the swapped image'''
    
    dst_img = cv2.imread(dest)

    # Select src face
    src_points, src_shape, src_face = select_face(src)
    # Select dst face
    dst_points, dst_shape, dst_face = select_face(dst_img)

    if src_points is None or dst_points is None:
        print('Detect 0 Face !!!')
        exit(-1)

    return face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img)

 
