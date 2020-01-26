import timeit
import xlwt
import cv2
from interpolants import nearest_neighbor

def create_interpolation_wrapper_callable( func, image, dim ):
    def wrapped_callable():
        return func( image, dim )
    return wrapped_callable

def create_worksheet( workbook, algorithm, images, dimensions  ):
    worksheet = workbook.add_sheet( algorithm[0] )

    for i in range( 0, len( images ) ):
        worksheet.write( 0, i + 1, images[i].split('/')[1] )

    for j in range( 0, len( dimensions ) ):
        worksheet.write( j + 1, 0, str( dimensions[j] ) )

    return worksheet

def time_tests( images, dimensions, average, algorithms, output_file ):
    workbook = xlwt.Workbook()
    style = xlwt.XFStyle()
    style.num_format_str = '0.000000'

    for alg_num in range( 0, len( algorithms ) ):
        curr_alg = algorithms[alg_num]
        worksheet = create_worksheet( workbook, curr_alg, images, dimensions )

        for img_num in range( 0, len( images ) ):
            curr_img = images[img_num]

            for dim_num in range( 0, len( dimensions ) ):
                curr_dim = dimensions[dim_num]
                image = cv2.imread( curr_img )
                
                callable_alg = curr_alg[1]
                wrapped_callable = create_interpolation_wrapper_callable( callable_alg, image, curr_dim )
                
                average_time = timeit.timeit(wrapped_callable, number=average)

                # change to ns
                average_time *= ( 10 ** 9 )
                average_time /= average
                worksheet.write( dim_num + 1, img_num + 1, average_time, style )

    workbook.save( output_file )


if __name__ == '__main__':
    # TODO: get better test images
    images = [
                'images/hat-guy.png'
             ] 
    
    num_avg = 1000
   
   # TODO: update this with better values
    dimensions = [
                    ( 32, 32 ),
                    ( 64, 64 ),
                    ( 128, 128 ),
                    ( 256, 256 ),
                    ( 512, 512 ),
                    ( 1024, 1024 ),
                    ( 2048, 2048 ),
                    ( 4096, 4096 )
                 ]

    algorithms = [
                    ( 'Nearest Neighbor CV', nearest_neighbor.scale_cv )
                 ]

    # This is just to test our algorithm before benchmarking it
    img = cv2.imread('images/hat-guy.png')
    new_img = nearest_neighbor.scale( img, dimensions[4] )
    cv2.imshow('image', new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Run the benchmark
    output_file = "Interpolation_Benchmark.xls"
    time_tests( images, dimensions, num_avg, algorithms, output_file )
