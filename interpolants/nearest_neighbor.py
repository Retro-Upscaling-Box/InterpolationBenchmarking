import cv2
import numpy

def scale( image, dim ):
    shape = image.shape
    print(shape)
    img = numpy.zeros( [dim[0], dim[1], 3], dtype=numpy.uint8 )
    for i in range( 0, dim[0] ):
        for j in range( 0, dim[1] ):
            if ( i < shape[0] and j < shape[1] ):
                img[i, j] = image[i, j]
    return img


def scale_cv( image, dim ):
    cv2.resize( image, dim, interpolation = cv2.INTER_NEAREST ) 
