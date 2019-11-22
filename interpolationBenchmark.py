import cv2
import numpy
 
image = cv2.imread( 'images/noah_16_4bit.png' )
img_size = image.shape

dimension = ( 30 * img_size[1], 30 * img_size[0] )
resized = cv2.resize( image, dimension, interpolation = cv2.INTER_NEAREST )

cv2.imshow( 'Original image', image )
cv2.imshow( 'Resized image', resized )
cv2.waitKey( 0 )
cv2.destroyAllWindows()

#TODO:
# create file structure where we can easily add algorithms to time
# create timing
# output results to csv or something
