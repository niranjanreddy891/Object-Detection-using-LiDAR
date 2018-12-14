# author: niranjanreddy891@gmail.com


from laspy.file import File
import numpy as np

inFile = File('E:/Lidar-practice/new-files/las14_type7_ALS_RIEGL_Q680i.las', mode='r')

I = inFile.Classification == 2

outFile = File('E:/Lidar-practice/new-files/tttttttttttt.pcd', mode='w', header=inFile.header)
outFile.points = inFile.points[I]
outFile.close()
