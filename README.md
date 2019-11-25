# Interpolation Benchmarking
----
## Algorithms to benchmark
### OpenCV And Rebuilt

1. Nearest Neighbor
2. Nonblurry integer-ratio scaling

----
## How To Add Tests
All you need to do is create an interpolation file in the interpolants folder that conaints the algorithms you want to test.
You can then import them in init.py and add them to the list of functions to test in main.
You can change or add images and dimensions to scale to by modifying the respective lists.
