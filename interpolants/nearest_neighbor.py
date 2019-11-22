import cv2
import numpy

def nearest_neighbor( img, dim ):
    return True

def nearest_neighbor_cv( img, dim ):
    image = cv2.imread( img )
    img_size = image.shape

    dimension = ( 30 * img_size[1], 30 * img_size[0] )
    resized = cv2.resize( image, dimension, interpolation = cv2.INTER_NEAREST )

    cv2.imshow( 'Original image', image )
    cv2.imshow( 'Resized image', resized )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()

