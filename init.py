import time
import xlwt
from interpolants import nearest_neighbor as nn

def create_worksheet( workbook, algorithm, images, dimensions  ):
    worksheet = workbook.add_sheet( algorithm.__name__ )

    for i in range( 0, len( images ) ):
        worksheet.write( 0, i + 1, images[i] )

    for j in range( 0, len( dimensions ) ):
        worksheet.write( j + 1, 0, str( dimensions[j] ) )

    return worksheet

def time_tests( images, dimensions, average, algorithms, output_file ):
    workbook = xlwt.Workbook()

    for alg_num in range( 0, len( algorithms ) ):
        curr_alg = algorithms[alg_num]
        worksheet = create_worksheet( workbook, curr_alg, images, dimensions )

        for img_num in range( 0, len( images ) ):
            curr_img = images[img_num]

            for dim_num in range( 0, len( dimensions ) ):
                curr_dim = dimensions[dim_num]
                average_time = 0

                for i in range( 0, average ):
                    t1 = time.time();
                    curr_alg( curr_img, curr_dim )
                    t2 = time.time();
                    dt = t2 - t1
                    average_time += dt
    
                average_time /= average
                worksheet.write( dim_num + 1, img_num + 1, str( average_time ) )

    workbook.save( output_file )


if __name__ == '__main__':
    images = [
                'images/hat-guy.png'
             ]
    
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
    
    num_avg = 10

    algorithms = [
                    nn.nearest_neighbor_cv
                 ]

    output_file = "Interpolation_Benchmark.xls"
    time_tests( images, dimensions, num_avg, algorithms, output_file )
