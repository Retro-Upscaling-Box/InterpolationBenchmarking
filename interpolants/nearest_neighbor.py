import cv2

def nearest_neighbor( image, dim ):
    return True

def nearest_neighbor_cv( image, dim ):
    cv2.resize( image, dim, interpolation = cv2.INTER_NEAREST ) 
