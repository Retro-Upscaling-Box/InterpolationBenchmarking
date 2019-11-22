import time
from interpolants import nearest_neighbor as nn

if __name__ == '__main__':
    image = 'images/noah_16_4bit.png'
    dimension = ( 30, 30 )

    num_avg = 10

    #TODO: maybe move this to a function to call
    for i in range( 1, num_avg ):
        t1 = time.time() 
        print( "test" )
        t2 = time.time()
        dt = t2 - t1

    nn.nearest_neighbor_cv( image, dimension )

#TODO:
# output results to csv or something
