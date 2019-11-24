import cv2
import numpy

def nearest_neighbor( img, dim ):
    return True

def nearest_neighbor_cv( img_path, dim ):
    image = cv2.imread( img_path )
    resized = cv2.resize( image, dim, interpolation = cv2.INTER_NEAREST ) 
