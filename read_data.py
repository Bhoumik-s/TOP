import numpy as np
import xlrd

def read(file):
    book = xlrd.open_workbook(file)
    worksheet = book.sheet_by_index(0)
    data=np.zeros((worksheet.nrows-1,worksheet.ncols),dtype=int)
    for i in range (worksheet.nrows-1):
        for j in range (worksheet.ncols):
            data[i][j]=worksheet.cell(i+1,j).value
    return data

def find_segments(points):
    distance=np.zeros((points.shape[0],points.shape[0]))
    for i in range(points.shape[0]):
        for j in range (i+1, points.shape[0]):
            distance[i][j]=pow(pow(points[i][0]-points[j][0],2)+pow(points[i][1]-points[j][1],2),0.5)
            distance[j][i]=distance[i][j]
    return distance

